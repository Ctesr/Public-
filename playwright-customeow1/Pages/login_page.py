from playwright.sync_api import Page, TimeoutError
from Components.login_component import LoginFormComponent
from Configs.env_config import EnvConfig
from Utils.Browserdriver import BrowserInstance


class LoginPage:
    """登录页面"""

    def __init__(self, page: Page):
        self.page = page
        self.login_form = LoginFormComponent(page)
        self.env_config = EnvConfig()

    def navigate(self):
        """导航到登录页"""
        base_url = self.env_config.get_base_url()
        self.page.goto(f"{base_url}/login")
        print('打开浏览器并导航到登录页')

    def email_click(self):
        """选择邮箱登录方式"""
        self.login_form.click_email()
        print("点击邮箱登录方式")

    def fill_credentials(self, username: str, password: str):
        """填写用户名和密码"""
        self.login_form.fill_username(username)
        print("输入账号")
        self.login_form.fill_password(password)
        print("输入密码")

    def submit_login(self):
        """提交登录表单"""
        self.login_form.click_submit()
        print("提交登录表单")

    def login_as_admin(self):
        """使用管理员账号登录"""
        self.navigate()
        self.email_click()
        self.fill_credentials("fjc@idd.cool", "Aa123456!")
        self.submit_login()
        print("管理员账号登录完成")


# # 如果你想通过 BrowserInstance 启动浏览器
# if __name__ == "__main__":
#     browser_instance = BrowserInstance(browser_type='chromium', headless=False)
#     page = browser_instance.start_browser()
#
#     login_page = LoginPage(page)
#     login_page.login_as_admin()
#
#     # 完成后关闭浏览器
#     browser_instance.close_browser()
