from playwright.sync_api import sync_playwright
import time


def auto_play_kuxueyuan(token_value):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # 这里模拟了设置一个头部信息，通常需要在浏览器的开发者工具里查看具体的 Authorization header
        context.set_extra_http_headers({
            'Authorization': f'Bearer {token_value}',  # 设置适当的认证头部
        })

        page = context.new_page()

        # 访问酷学院首页
        page.goto("https://pro.coolcollege.cn/index.html#/home")

        # 等待页面加载
        time.sleep(5)

        # 等待页面完全加载，确保所有课程数据和视频都能正常访问
        page.wait_for_selector('button.play')

        # 查找并点击播放按钮
        while True:
            try:
                # 查找播放按钮并点击（如果存在）
                play_button = page.query_selector("button.play")
                if play_button:
                    play_button.click()
                    print("点击播放按钮")
                    time.sleep(2)

                # 检测视频是否在播放（可以根据 class 变化或时间轴进度检测）
                video_element = page.query_selector("video")
                if video_element:
                    current_time = page.evaluate("document.querySelector('video').currentTime")
                    duration = page.evaluate("document.querySelector('video').duration")
                    print(f"视频播放进度: {current_time:.2f}/{duration:.2f}")

                    if duration - current_time < 5:  # 如果视频即将结束
                        print("即将播放下一个视频...")
                        next_button = page.query_selector("button.next")
                        if next_button:
                            next_button.click()
                            time.sleep(5)
                            continue

                # 处理可能的弹窗（如确认框）
                if page.query_selector("button.confirm"):
                    page.click("button.confirm")
                    print("已点击确认按钮")
                    time.sleep(2)

                time.sleep(5)
            except Exception as e:
                print(f"发生错误: {e}")
                break

        browser.close()


if __name__ == "__main__":
    # 输入 Token 值，进行自动登录
    token_value = input("请输入你的 Token 值: ")
    auto_play_kuxueyuan(token_value)
