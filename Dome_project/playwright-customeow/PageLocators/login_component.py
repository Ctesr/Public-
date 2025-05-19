from playwright.sync_api import Page
# from utils.logger import get_logger


class LoginFormComponent:
    """登录表单组件"""

    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.get_by_placeholder("输入您的电子邮箱")
        self.password_input = page.get_by_placeholder("输入您的密码")
        self.submit_button = page.locator('button[type="submit"]')

    # def fill_username(self, username: str):
    #     """输入用户名"""
    #     # self.logger.info(f"输入用户名: {username}")
    #     self.email_input.fill(username)
    #
    # def fill_password(self, password: str):
    #     """输入密码"""
    #     # self.logger.info(f"输入密码: {password}")
    #     self.password_input.fill(password)
    #
    # def click_submit(self):
    #     """点击登录按钮"""
    #     # self.logger.info("点击登录按钮")
    #     self.submit_button.click()