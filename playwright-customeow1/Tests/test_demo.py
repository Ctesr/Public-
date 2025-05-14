# tests/test_browser.py
from pathlib import Path
from Configs.logger_config import configure_logger
from Utils.Browserdriver import BrowserInstance

project_logger = configure_logger(
    name="E2E_Tests",
    log_level="DEBUG",
    log_file=Path("logs/e2e_tests.log")
)


def test_browser_operations():
    # 初始化浏览器实例并传入日志器
    browser_manager = BrowserInstance(
        browser_type="chromium",
        headless=False,
        logger=project_logger.getChild("BrowserInstance"),  # 继承父日志器
        log_level="DEBUG"
    )

    page = browser_manager.start_browser()
    if page:
        if browser_manager.open_url("https://example.com"):
            project_logger.info("页面打开成功，执行后续操作...")
        browser_manager.close_browser()


if __name__ == "__main__":
    test_browser_operations()