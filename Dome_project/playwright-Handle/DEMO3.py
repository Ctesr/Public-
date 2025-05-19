import asyncio
import random
import time
import pandas as pd
from tqdm import tqdm
from playwright.async_api import async_playwright
import traceback

# === 配置区 ===
base_url = "https://ca.giftlab.com/products/"

excel_file = r"D:\JCtestgit\Dome_project\playwright-Handle\failed4.xlsx"
failed_urls_file = "failed5.xlsx"
ok_file = "OK5.xlsx"
proxy_server = "http://127.0.0.1:7897"
concurrency = 15  # 每批处理数量
retry_count = 2   # 页面加载失败/点击失败的最大重试次数

# === 查找并点击目标元素 ===
async def find_element(page, selectors, url, full_url):
    for selector in selectors:
        try:
            locator = page.locator(selector)
            count = await locator.count()
            if count > 0:
                print(f"{url} 🎯 找到元素：{selector}（{count} 个）")
                await page.wait_for_selector(selector, timeout=300000, state="visible")
                try:
                    await locator.nth(0).click(timeout=50000)
                    print(f"{full_url} ✅ 点击成功：{selector}")
                    return True
                except Exception as e:
                    print(f"{full_url} ⚠️ 点击失败：{selector}, 错误: {e}")
        except Exception as e:
            print(f"{full_url} ⚠️ 查找元素异常：{selector}, 错误: {e}")
    print(f"{url} ❌ 没有找到可点击的目标元素")
    return False

# === 处理单个页面 ===
async def process_url(sem, context, url, exist_urls, not_exist_urls):
    async with sem:
        full_url = base_url + str(url)
        page = await context.new_page()

        try:
            print(f"🚀 访问: {full_url}")
            for attempt in range(retry_count):
                try:
                    await page.goto(full_url, timeout=600000, wait_until="domcontentloaded")
                    await asyncio.sleep(random.uniform(0.5, 1.5))
                    await page.wait_for_selector("main#MainContent", timeout=280000)

                    selectors = [
                        "div.__sunzi_customeow>div.__button",
                        "div.__sunzi_customeow",
                        "div.sunzi__button-s-s1R",
                        "div.__custom_button_wrapper",
                        "button#sunzi-button"
                    ]

                    success = await find_element(page, selectors, url,full_url)
                    if success:
                        exist_urls.append(full_url)
                    else:
                        not_exist_urls.append(full_url)
                        print(f"❌ 该页面不包含目标元素： {full_url}")
                    break
                except Exception as e:
                    print(f"⚠️ 第 {attempt+1} 次访问失败: {full_url}, 错误: {e}")
                    traceback.print_exc()
                    if attempt == retry_count - 1:
                        not_exist_urls.append(full_url)
        finally:
            try:
                await page.close()
            except Exception:
                pass

# === 主流程 ===
async def run():
    start = time.time()
    df = pd.read_excel(excel_file)
    # urls = df["Handle"].astype(str).tolist()
    urls = df["Handle"].astype(str).str.strip().tolist()

    sem = asyncio.Semaphore(concurrency)
    exist_urls = []
    not_exist_urls = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, proxy={"server": proxy_server})
        context = await browser.new_context(user_agent="Mozilla/5.0 ... Chrome/120.0.0.0 Safari/537.36")

        total = len(urls)
        progress_bar = tqdm(total=total, desc="处理进度")

        async def wrapped_task(url):
            await process_url(sem, context, url, exist_urls, not_exist_urls)
            progress_bar.update(1)

        for i in range(0, total, concurrency):
            batch = urls[i:i + concurrency]
            print(f"\n📦 第 {i // concurrency + 1} 批（{len(batch)} 个）开始...\n")
            await asyncio.gather(*(wrapped_task(url) for url in batch))

        progress_bar.close()
        await context.close()
        await browser.close()

    # 保存结果
    pd.DataFrame({"OK URL": exist_urls}).to_excel(ok_file, index=False)
    print(f"✅ 成功 URL 保存: {ok_file}")

    pd.DataFrame({"Failed URL": not_exist_urls}).to_excel(failed_urls_file, index=False)
    print(f"🚫 失败 URL 保存: {failed_urls_file}")

    duration = time.time() - start
    print(f"\n✅ 全部完成，总耗时: {duration:.2f} 秒")

# === 运行入口 ===
if __name__ == "__main__":
    asyncio.run(run())
