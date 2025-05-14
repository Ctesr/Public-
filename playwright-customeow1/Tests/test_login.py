# # test_login.py
# from playwright.sync_api import expect
# from Pages.login_page import LoginPage
# from playwright.sync_api import Playwright, sync_playwright, expect
#
# def test_admin_login(playwright: Playwright):
#     # 初始化页面对象
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     login_page = LoginPage(page)
#     login_page.navigate()
#
#     # 执行登录操作
#     login_page.login_as_admin()
#
#     # 验证登录结果
#     expect(page).to_have_url("https://beta-customeow.maiyuan.online/zh-cn/store")


from playwright.sync_api import expect, Page, Playwright, sync_playwright
from Pages.login_page import LoginPage
from Utils.Browserdriver import BrowserInstance


def test_admin_login(page: Page):
    # 使用 BrowserInstance 启动浏览器并创建页面
    page = page

    # 初始化页面对象
    login_page = LoginPage(page)

    # 导航到登录页面
    login_page.navigate()

    # 执行登录操作
    login_page.login_as_admin()

    # 确保页面跳转完成并验证 URL
    expect(page).to_have_url("https://beta-customeow.maiyuan.online/zh-cn/store")

