from playwright.sync_api import sync_playwright

# class BrowserInstance:
#     """浏览器实例管理"""
#
#     def __init__(self, browser_type='chromium', headless=False):
#         self.browser_type = browser_type
#         self.headless = headless
#         self.browser = None
#         self.context = None
#         self.page = None
#         self.playwright = None
#
#     def start_browser(self):
#         """启动浏览器并返回页面对象"""
#         self.playwright = sync_playwright().start()  # 手动启动 Playwright 实例
#         if self.browser_type == 'chromium':
#             self.browser = self.playwright.chromium.launch(headless=self.headless)
#         elif self.browser_type == 'firefox':
#             self.browser = self.playwright.firefox.launch(headless=self.headless)
#         elif self.browser_type == 'webkit':
#             self.browser = self.playwright.webkit.launch(headless=self.headless)
#         else:
#             raise ValueError(f"Unsupported browser type: {self.browser_type}")
#
#         self.context = self.browser.new_context()
#         self.page = self.context.new_page()
#         return self.page
#
#     def open_url(self):
#         """打开页面"""
#         try:
#             self.page.goto(self.env_config.get_login_url())
#             print("页面已打开")
#         except TimeoutError:
#             print("页面加载超时，请检查网络连接")
#
#     def close_browser(self):
#         """关闭浏览器并停止 Playwright 实例"""
#         if self.browser:
#             self.browser.close()
#         if self.playwright:
#             self.playwright.stop()  # 停止 Playwright 实例


# browser_instance.py
from playwright.sync_api import sync_playwright
from pathlib import Path
from typing import Optional
import logging
from Configs.logger_config import configure_logger  # 导入日志配置


class BrowserInstance:
    """浏览器实例管理（集成日志功能）"""

    def __init__(
            self,
            browser_type: str = 'chromium',
            headless: bool = False,
            logger: Optional[logging.Logger] = None,
            log_screenshots: bool = True,
            screenshot_dir: Path = Path("logs/screenshots"),
            log_level: str = "INFO"
    ):
        """
        参数：
        browser_type: 浏览器类型 (chromium/firefox/webkit)
        headless: 是否无头模式
        logger: 自定义日志记录器，若未提供则自动创建
        log_screenshots: 是否在错误时截图
        screenshot_dir: 截图保存目录
        log_level: 日志级别 (DEBUG/INFO/WARNING/ERROR)
        """
        self.browser_type = browser_type
        self.headless = headless
        self.log_screenshots = log_screenshots
        self.screenshot_dir = screenshot_dir

        # 初始化日志
        self.logger = logger or configure_logger(
            name=__name__,
            log_level=log_level,
            log_file=Path("logs/browser_operations.log")  # 默认日志文件路径
        )

        # 浏览器实例
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

        # 初始化目录
        self._init_directories()

    def _init_directories(self) -> None:
        """创建必要目录"""
        self.screenshot_dir.mkdir(parents=True, exist_ok=True)
        self.logger.debug("目录已创建: %s", self.screenshot_dir)

    def start_browser(self) -> Optional['Page']:
        """启动浏览器并返回页面对象"""
        try:
            self.logger.info("启动 Playwright 实例...")
            self.playwright = sync_playwright().start()

            self.logger.info("启动 %s 浏览器 (无头模式: %s)", self.browser_type, self.headless)
            browser_launcher = getattr(self.playwright, self.browser_type)
            self.browser = browser_launcher.launch(headless=self.headless)

            self.context = self.browser.new_context()
            self.page = self.context.new_page()
            return self.page
        except Exception as e:
            self.logger.error("浏览器启动失败: %s", str(e), exc_info=True)
            self._capture_screenshot("browser_start_failure")
            return None

    def open_url(self, url: str, timeout: float = 30000) -> bool:
        """打开指定 URL"""
        try:
            self.logger.info("正在打开 URL: %s", url)
            response = self.page.goto(url, timeout=timeout)
            if response and response.ok:
                self.logger.debug("页面加载成功 (状态码: %d)", response.status)
                return True
            self.logger.warning("页面加载异常 (状态码: %s)", response.status if response else "N/A")
            return False
        except Exception as e:
            self.logger.error("打开页面失败: %s", str(e), exc_info=True)
            self._capture_screenshot("page_load_failure")
            return False

    def close_browser(self) -> None:
        """安全关闭浏览器实例"""
        try:
            if self.browser:
                self.logger.info("关闭浏览器...")
                self.browser.close()
            if self.playwright:
                self.playwright.stop()
            self.logger.info("浏览器实例已安全关闭")
        except Exception as e:
            self.logger.error("关闭过程中发生错误: %s", str(e), exc_info=True)

    def _capture_screenshot(self, prefix: str) -> None:
        """捕获错误截图"""
        if not self.log_screenshots or not self.page:
            return
        try:
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = self.screenshot_dir / f"{prefix}_{timestamp}.png"
            self.page.screenshot(path=str(screenshot_path))
            self.logger.info("截图已保存至: %s", screenshot_path)
        except Exception as e:
            self.logger.error("截图保存失败: %s", str(e))