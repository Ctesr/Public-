from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False, args=[
#                 '--disable-blink-features=AutomationControlled',
#                 '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
#             ])
#     context = browser.new_context()
# #     context.add_cookies([
#         {"name": "cto_bundle", "value": "vbVq6l9mUlRaUmhBZGg0b1BVZkhwcTZiVWswdkQlMkJRJTJCSElrbWpMeGNWaWZBNlIlMkZVMXhyTWFIZnY5Y3Y2bHdNWVR6czJ1eUNpczZReFdvNWxoaDF5ejFmaTVFVnJDczQyZ0Q0Y21JMmtrWFE1MDNPZTJqdGNGMjV3QWk4cDRGNVFrelpmanN4cW9kaEpBeUdNTkNSVXU3RWlTZkElM0QlM0Q", "domain": ".spotidownloader.com"},
#         {"name": "uid", "value": "81dc30c8-963d-494a-8c91-8f5beade3f16", "domain": ".spotidownloader.com"}
#     ])

#     page = context.new_page()
#     page.goto("https://spotidownloader.com/")
#     page.get_by_placeholder("https://open.spotify.com/.../").click()
#     page.get_by_placeholder("https://open.spotify.com/.../").fill("https://open.spotify.com/track/4J1vA4sgG6FJ1j21UugbtH?si=b5a4643670914918")
#     page.wait_for_timeout(50000)
#     # 暂停脚本，手动完成验证
#     print("请手动完成人机验证，完成后按回车继续...")
#     input()  # 等待用户操作
#
#     # 继续后续操作（如点击Convert按钮）
#     page.click("button:has-text('Convert')")
#
#     # ---------------------
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     run(playwright)


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, args=[
        '--disable-blink-features=AutomationControlled',
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    ])
    context = browser.new_context()

    # 添加 Cloudflare 验证通过的 Cookie
    context.add_cookies([
                {"name": "cto_bundle", "value": "vbVq6l9mUlRaUmhBZGg0b1BVZkhwcTZiVWswdkQlMkJRJTJCSElrbWpMeGNWaWZBNlIlMkZVMXhyTWFIZnY5Y3Y2bHdNWVR6czJ1eUNpczZReFdvNWxoaDF5ejFmaTVFVnJDczQyZ0Q0Y21JMmtrWFE1MDNPZTJqdGNGMjV3QWk4cDRGNVFrelpmanN4cW9kaEpBeUdNTkNSVXU3RWlTZkElM0QlM0Q", "domain": ".spotidownloader.com","path": "/"},
                {"name": "uid", "value": "81dc30c8-963d-494a-8c91-8f5beade3f16", "domain": ".spotidownloader.com","path": "/"}
    ])

    page = context.new_page()
    page.goto("https://spotidownloader.com/")

    page.get_by_placeholder("https://open.spotify.com/.../").click()
    page.get_by_placeholder("https://open.spotify.com/.../").fill(
        "https://open.spotify.com/track/4J1vA4sgG6FJ1j21UugbtH?si=b5a4643670914918")

    print("请手动完成人机验证，完成后按回车继续...")
    input()

    page.click("button:has-text('Convert')")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
