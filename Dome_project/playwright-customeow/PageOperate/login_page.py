from playwright.sync_api import Page
from PageLocators.login_component import LoginFormComponent


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

    def fill_credentials(self, username: str, password: str):
        """填写用户名和密码"""
        self.login_form.password_input(username)
        self.login_form.password_input(password)

    def submit_login(self):
        """提交登录表单"""
        # self.login_form.click_submit()

    def login_as_admin(self):
        """使用管理员账号登录"""
        self.fill_credentials("fjc@idd.cool", "Aa123456!")
        self.submit_login()