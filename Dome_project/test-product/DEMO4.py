import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import time
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import os

# 弹窗输入 URL 前缀 + 选择文件，放在同一窗口
def get_user_input():
    root = tk.Tk()
    root.title("输入基础 URL 和选择文件")

    # 设置窗口大小和固定大小
    root.geometry("400x250")
    root.resizable(False, False)

    # 设置窗口背景色
    root.config(bg="#f0f0f0")

    # 设置字体
    label_font = ("Arial", 12)
    entry_font = ("Arial", 10)

    # 创建基础 URL 标签和输入框
    label_url = tk.Label(root, text="请输入域名，如：https://www.giftlab.com/products/", font=label_font, bg="#f0f0f0")
    label_url.pack(pady=(20, 5))

    entry_url = tk.Entry(root, font=entry_font, width=40, bd=2, relief="solid")
    entry_url.pack(pady=5)

    # 创建选择文件按钮
    def choose_file():
        file_path = filedialog.askopenfilename(title="选择 Handle.xlsx 文件", filetypes=[("Excel Files", "*.xlsx")])
        if file_path:
            file_var.set(file_path)

    file_var = tk.StringVar()
    file_button = ttk.Button(root, text="选择 Handle.xlsx 文件", command=choose_file, width=20)
    file_button.pack(pady=10)

    file_label = tk.Label(root, textvariable=file_var, font=("Arial", 9), bg="#f0f0f0", fg="#0078D4")
    file_label.pack(pady=5)

    # 创建提交按钮
    def on_submit():
        domain = entry_url.get()
        file_path = file_var.get()
        if not domain or not file_path:
            messagebox.showerror("错误", "请确保输入了所有信息！")
            return
        root.quit()
        root.destroy()  # 关闭窗口
        global user_input
        user_input = (domain, file_path)

    submit_button = ttk.Button(root, text="提交", command=on_submit, width=20)
    submit_button.pack(pady=(10, 20))

    root.mainloop()

    return user_input

# 读取指定的 Handle.xlsx 文件并取 Handle 列
def get_urls_from_file(file_path):
    if not os.path.exists(file_path):
        print(f"❌ 找不到文件: {file_path}")
        exit()

    df = pd.read_excel(file_path)
    if "Handle" not in df.columns:
        print("❌ 文件中没有 'Handle' 列")
        exit()

    return df["Handle"].astype(str).tolist()


async def find_element(page, selectors):
    for selector in selectors:
        locator = page.locator(selector)
        if await locator.count() > 0:
            try:
                await locator.click()
                return locator
            except Exception as e:
                print(f"⚠️ 点击失败: {selector}, 错误: {e}")
                return None
    return None


async def process_url(sem, context, url, base_url, exist_urls, not_exist_urls):
    async with sem:
        full_url = base_url + str(url)
        page = await context.new_page()
        try:
            print(f"访问: {full_url}")
            await page.goto(full_url, timeout=580000, wait_until="networkidle")
            await page.wait_for_selector("main#MainContent")
            selectors = [
                "div.__sunzi_customeow",
                "div.sunzi__button-s-s1R",
                "div.__custom_button_wrapper",
                "button#sunzi-button",
            ]
            element = await find_element(page, selectors)
            if element:
                exist_urls.append(full_url)
                print(f"✅ 包含元素: {full_url}")
            else:
                not_exist_urls.append(full_url)
                print(f"❌ 不包含元素: {full_url}")
        except Exception as e:
            print(f"⚠️ 错误: {full_url}, 错误: {e}")
            not_exist_urls.append(full_url)
        finally:
            await page.close()


async def run():
    base_url, file_path = get_user_input()  # 获取用户输入的 URL 和文件路径
    urls = get_urls_from_file(file_path)

    exist_urls = []
    not_exist_urls = []
    sem = asyncio.Semaphore(25)

    start_time = time.time()

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()

        for i in range(0, len(urls), 25):
            batch = urls[i:i + 25]
            tasks = [process_url(sem, context, url, base_url, exist_urls, not_exist_urls) for url in batch]
            await asyncio.gather(*tasks)

        await context.close()
        await browser.close()

    df_ok = pd.DataFrame({"URL": exist_urls})
    df_ok.to_excel(os.path.join(os.path.dirname(file_path), "Handle-OK.xlsx"), index=False)

    df_fail = pd.DataFrame({"URL": not_exist_urls})
    df_fail.to_excel(os.path.join(os.path.dirname(file_path), "Handle-failed.xlsx"), index=False)

    print(f"\n✅ 任务完成，总耗时: {time.time() - start_time:.2f} 秒")


if __name__ == "__main__":
    asyncio.run(run())
