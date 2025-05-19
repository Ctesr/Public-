# test_login.py
from playwright.sync_api import expect
from PageOperate.login_page import LoginPage


def test_admin_login(page):
    # 初始化页面对象
    login_page = LoginPage(page)
    login_page.navigate()

    # 执行登录操作
    login_page.login_as_admin()

    # 验证登录结果
    expect(page).to_have_url("/store")
