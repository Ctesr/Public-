from playwright.sync_api import sync_playwright

class BrowserManager:
    def __init__(self, headless=True):
        self.headless = headless
        self.browser = None
        self.context = None
        self.page = None
        self.playwright = None  # 确保 Playwright 生命周期管理

    def launch_browser(self):
        """启动浏览器并创建上下文"""
        self.playwright = sync_playwright().start()  # 修正 Playwright 生命周期管理
        self.browser = self.playwright.chromium.launch(headless=self.headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def close_browser(self):
        """关闭浏览器"""
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()  # 关闭 Playwright 实例，避免资源泄露

    def get_browser(self):
        """返回 Browser 实例"""
        return self.browser

    def get_page(self):
        """返回 Page 实例"""
        return self.page
