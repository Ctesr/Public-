from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://customeow.io/zh-cn/login")
    print('打开网页')
    page.get_by_text("使用电子邮箱登录").click()
    # page.locator("span.cm-flex.cm-items-center").click()
    print('点击电子邮箱')
    # page.get_by_text("输入您的电子邮箱").click()
    page.get_by_placeholder("输入您的电子邮箱").fill("fjc@idd.cool")
    print('输入账号')
    page.locator("#password_input").fill("Aa123456!")
    print('输入密码')
    page.locator('button[type="submit"]').click()
    print('点击登陆')
    page.wait_for_timeout(10000)
    assert page.url == "/login"

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)