import asyncio
import os
from tqdm.asyncio import tqdm_asyncio
import random
import pandas as pd
from playwright.async_api import async_playwright
import time
from tqdm.asyncio import tqdm
# 基础 URL
base_url = "https://www.giftlab.de/products/"
# 读取 Excel 文件
excel_file = r"D:\JCtestgit\Dome_project\playwright-Handle\failed7.xlsx"

df = pd.read_excel(excel_file)
urls = df["Handle"].astype(str).tolist()

# 失败的 URL 存储文件
failed_urls_file = "failed8.xlsx"
#成功
OK = "OK8.xlsx"

# 限制并发任务数
BATCH_SIZE = 10



async def find_element(page, selectors, url):
    """查找多个元素中的第一个存在的元素并点击"""
    for selector in selectors:
        locator = page.locator(selector)
        count = await locator.count()
        if count > 0:
            print(f"{url} 找到元素：{selector}（共 {count} 个）")
            await page.wait_for_selector(selector, timeout=300000, state="visible")
            try:
                await locator.nth(0).click(timeout=10000)  # 点击第一个
                print(f"{url} ✅ 点击成功：{selector}")
                return locator
            except Exception as e:
                print(f"⚠️ {url} ❌ 点击失败：{selector}, 错误: {e}")
                continue  # 继续尝试下一个 selector

    print(f"{url} ❌ 没有找到可点击的目标元素")
    return None


async def process_url(sem, context, url, exist_urls, not_exist_urls):
    """处理单个 URL，使用同一个浏览器窗口打开多个标签页"""

    async with sem:  # 控制并发
        full_url = base_url + str(url)
        page = await context.new_page()  # 在相同的浏览器实例中打开新标签页
        try:
            print(f"访问: {full_url}")
            start_time = time.time()  # 记录访问开始时间

            try:
                await page.goto(full_url, timeout=600000, wait_until="domcontentloaded")
                await asyncio.sleep(random.uniform(0.5, 1.5))  # 模拟人工延迟
                await page.wait_for_selector("main#MainContent")
                # print(r" <main> 元素加载完成")

                selectors = [
                    "div.__sunzi_customeow>div.__button",
                    "div.__sunzi_customeow",
                    "div.sunzi__button-s-s1R",
                    "div.__custom_button_wrapper",
                    "button#sunzi-button",

                    # "div.custom-design-row"
                ]

                # print("开始查找目标元素", full_url)
                success = await find_element(page, selectors, url)


                if success:
                    exist_urls.append(full_url)
                    print(f"✅ 该页面包含目标元素 {full_url}")
                else:
                    not_exist_urls.append(full_url)
                    print(f"❌ 该页面不包含目标元素： {full_url}")

            except Exception as e:
                print(f"⚠️ 访问失败: {full_url}, 错误: {e}")
                not_exist_urls.append(full_url)

        finally:
            if not page.is_closed():
                await page.close()  # 关闭该标签页

async def run():
    start_time = time.time()  # 记录开始时间
    """主函数，使用单个浏览器窗口并在其中打开多个标签页"""
    # 配置代理参数
    proxy_settings = {
        "server": "http://127.0.0.1:7897",  # 代理本地地址和端口
    }
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(
                headless=True,
                proxy=proxy_settings
            )
        context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        total = len(urls)
        exist_urls = []
        not_exist_urls = []
        sem = asyncio.Semaphore(BATCH_SIZE)  # 限制同时打开的标签页数
        completed = 0
        progress_bar = tqdm(total=total, desc="整体进度")  # ✅ 总进度条

        async def wrapped_task(url):
            await process_url(sem, context, url, exist_urls, not_exist_urls)
            progress_bar.update(1)

        for i in range(0, total, BATCH_SIZE):
            batch = urls[i:i + BATCH_SIZE]
            print(f"\n🚀 运行第 {i // BATCH_SIZE + 1} 批，共 {len(batch)} 个 URL...\n")

            # 替换为 wrapped_task 包裹形式
            await asyncio.gather(*(wrapped_task(url) for url in batch))

            completed += len(batch)
            print(f"已处理: {completed}/{total}")

        progress_bar.close()  # ✅ 关闭进度条

        await context.close()
        await browser.close()

        # 记录失败的 URL

        # 失败
        df_failed = pd.DataFrame({"Failed URL": not_exist_urls})
        df_failed.to_excel(failed_urls_file, index=False)
        print(f"🚫 失败 URL Excel 保存到 {failed_urls_file}")

        # 成功
        df_ok = pd.DataFrame({"OK URL": exist_urls})
        df_ok.to_excel(OK, index=False)
        print(f"✅ 成功 URL Excel 保存到 {OK}")

        end_time = time.time()  # 记录结束时间
        total_time = end_time - start_time
        print(f"\n✅ 全部任务完成，总耗时: {total_time:.2f} 秒")

# 运行 asyncio
asyncio.run(run())
