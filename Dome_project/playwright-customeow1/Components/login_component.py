from playwright.sync_api import Page
# from utils.logger import get_logger
from Configs.env_config import EnvConfig

class LoginFormComponent:
    """登录表单组件"""

    def __init__(self, page: Page):
        self.page = page
        self.env_config = EnvConfig()
        self.env_config.set_env("env_BETA")
        self.email_input = page.get_by_placeholder("输入您的电子邮箱")
        self.password_input = page.get_by_placeholder("输入您的密码")
        self.submit_button = page.locator('button[type="submit"]')
        self.email_button = page.get_by_text("使用电子邮箱登录")

    def click_email(self):
        """点击邮件登陆"""
        self.email_button.click()

    def fill_username(self, username: str):
        """输入用户名"""
        # self.logger.info(f"输入用户名: {username}")
        self.email_input.fill(username)

    def fill_password(self, password: str):
        """输入密码"""
        # self.logger.info(f"输入密码: {password}")
        self.password_input.fill(password)

    def click_submit(self):
        """点击登录按钮"""
        # self.logger.info("点击登录按钮")
        self.submit_button.click()



"""
from playwright.sync_api import Page, Locator, expect
from typing import Optional
import logging
from Configs.env_config import EnvConfig


class LoginFormComponent:
   
    # 登录表单组件，封装登录页面的所有交互逻辑。
    #
    # 特性：
    # - 支持动态环境配置
    # - 元素定位器集中管理
    # - 自动等待元素可见性
    # - 结构化日志记录
    # - 异常处理和错误截图
    #
    # 参数：
    # page (Page): Playwright 页面对象
    # env_config (EnvConfig): 环境配置对象
    # logger (Logger, optional): 日志记录器，默认为根日志器
    # timeout (int, optional): 元素等待超时时间（毫秒），默认为 10000
    

    定位器配置字典，格式: {"元素名": ("定位类型", "定位值")}
    LOCATORS = {
        "email_input": ("placeholder", "输入您的电子邮箱"),
        "password_input": ("placeholder", "输入您的密码"),
        "submit_button": ("css", 'button[type="submit"]'),
        "email_button": ("text", "使用电子邮箱登录"),
    }

    def __init__(
        self,
        page: Page,
        env_config: EnvConfig,
        logger: Optional[logging.Logger] = None,
        timeout: int = 10000
    ):
     
        初始化登录组件

        参数：
        page: Playwright 页面对象
        env_config: 环境配置对象，包含当前环境信息
        logger: 日志记录器，用于输出调试和错误信息
        timeout: 元素操作默认等待超时时间
     
        self.page = page
        self.env_config = env_config
        self.logger = logger or logging.getLogger(__name__)
        self.timeout = timeout

        # 动态初始化所有定位器
        self.email_input = self._get_locator(*self.LOCATORS["email_input"])
        self.password_input = self._get_locator(*self.LOCATORS["password_input"])
        self.submit_button = self._get_locator(*self.LOCATORS["submit_button"])
        self.email_button = self._get_locator(*self.LOCATORS["email_button"])

    def _get_locator(self, by: str, value: str) -> Locator:
       
        根据定位类型生成 Playwright 定位器

        参数：
        by: 定位类型，支持 'placeholder'/'text'/'css'
        value: 定位值

        返回：
        Locator: Playwright 元素定位器

        抛出：
        ValueError: 不支持的定位类型
      
        if by == "placeholder":
            return self.page.get_by_placeholder(value)
        elif by == "text":
            return self.page.get_by_text(value)
        elif by == "css":
            return self.page.locator(value)
        else:
            raise ValueError(f"不支持的定位器类型: {by}")

    def _wait_visible(self, element: Locator) -> None:
       
        等待元素可见，用于增强操作稳定性

        参数：
        element: 要等待的元素定位器
        
        element.wait_for(state="visible", timeout=self.timeout)
        self.logger.debug(f"元素可见性验证通过: {element}")

    def click_email(self) -> None:
        点击 '使用电子邮箱登录' 入口按钮
        self._wait_visible(self.email_button)
        self.email_button.click()
        self.logger.info("已点击邮箱登录入口")

    def fill_username(self, username: str) -> None:
        
        填充用户名/邮箱输入框

        参数：
        username: 要输入的用户名或邮箱
        
        self._wait_visible(self.email_input)
        self.email_input.fill(username)
        self.logger.info(f"已输入用户名: {username}")

    def fill_password(self, password: str) -> None:
       
        填充密码输入框

        参数：
        password: 要输入的密码
      
        self._wait_visible(self.password_input)
        self.password_input.fill(password)
        self.logger.info("已输入密码")

    def click_submit(self) -> None:
        点击登录提交按钮
        self._wait_visible(self.submit_button)
        self.submit_button.click()
        self.logger.info("已提交登录表单")

    def login(self, username: str, password: str) -> bool:
       
        执行完整登录流程

        参数：
        username: 用户名/邮箱
        password: 密码

        返回：
        bool: 登录是否成功 (True/False)
        
        try:
            self.logger.info(f"开始登录流程 | 环境: {self.env_config.current_env}")
            self.click_email()
            self.fill_username(username)
            self.fill_password(password)
            self.click_submit()
            return True
        except Exception as e:
            self.logger.error(f"登录失败: {str(e)}", exc_info=True)
            # 截屏保存错误现场，文件名包含环境信息
            screenshot_path = f"login_error_{self.env_config.current_env}.png"
            self.page.screenshot(path=screenshot_path)
            self.logger.debug(f"错误截图已保存至: {screenshot_path}")
            return False

    def expect_error_message(self, message: str) -> None:
        
        验证错误提示信息

        参数：
        message: 期望的错误提示文本

        抛出：
        AssertionError: 当实际文本不匹配时
       
        error_locator = self.page.locator(".error-message")
        expect(error_locator).to_have_text(message)
        self.logger.info(f"已验证错误提示: {message}")

    def is_email_login_available(self) -> bool:
        
        检查邮箱登录入口是否可用

        返回：
        bool: 是否可见且可点击
       
        return self.email_button.is_visible() and self.email_button.is_enabled()


from playwright.sync_api import sync_playwright
        
from Configs.env_config import EnvConfig
        
        # 初始化环境配置
        env_config = EnvConfig()
        env_config.set_env("env_BETA")  # 设置为测试环境
        
        # 配置日志
        logging.basicConfig(level=logging.INFO)
        
        with sync_playwright() as p:
            # 启动浏览器
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
        
            # 导航到登录页
            page.goto(env_config.login_url)
        
            # 创建登录组件实例
            login_component = LoginFormComponent(
                page=page,
                env_config=env_config,
                timeout=15000  # 延长超时时间
            )
        
            # 检查邮箱登录是否可用
            if login_component.is_email_login_available():
                # 执行登录流程
                success = login_component.login("test@example.com", "securePassword123")
        
                if success:
                    print("登录成功！")
                    # 后续业务操作...
                else:
                    print("登录失败，请检查日志和截图")
            else:
                print("邮箱登录入口不可用")
        
            browser.close()
        
        """