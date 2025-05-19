

from playwright.sync_api import Page, Locator

from typing import Optional


class BaseComponent:
    """组件基类，封装公共操作"""

    def __init__(self, page: Page, selector: str, parent: Optional[Locator] = None):
        self.page = page
        self.selector = selector
        self.parent = parent or page  # 父定位器，支持嵌套组件

    @property
    def root(self) -> Locator:
        """组件的根元素定位器"""
        return self.parent.locator(self.selector)

    """内置定位"""
    #
    # def t1(self, child_selector: str, name: str):
    #     '''按显式和隐式辅助功能属性进行定位。'''
    #     self.page.get_by_role(child_selector, name=name)

    def t2(self, child_selector: str):
        '''按文本内容进行定位。'''
        self.page.get_by_text(child_selector)

    def t3(self, child_selector: str):
        '''按关联标签的文本查找表单控件。'''
        self.page.get_by_label(child_selector)

    def t4(self, child_selector: str):
        '''按占位符查找输入。'''
        self.page.get_by_placeholder(child_selector)

    def t5(self, child_selector: str):
        '''通过其替代文本来定位元素，通常是 image。'''
        self.page.get_by_alt_text(child_selector)

    def t6(self, child_selector: str):
        '''按元素的title属性查找元素。'''
        self.page.get_by_title(child_selector)

    def t7(self, child_selector: str):
        '''根据元素的data - testid属性（可以配置其他属性）来定位元素。'''
        self.page.get_by_test_id(child_selector)








    def wait_until_visible(self, timeout: int = 10000) -> None:
        """等待组件可见"""
        self.root.wait_for(state="visible", timeout=timeout)

    def click(self, child_selector: str) -> None:
        """点击组件内的子元素"""
        self.root.locator(child_selector).click()

    def fill(self, child_selector: str, text: str) -> None:
        """填充输入框"""
        self.root.locator(child_selector).fill(text)

    def expect_text(self, child_selector: str, text: str) -> None:
        """验证子元素文本"""
        expect(self.root.locator(child_selector)).to_have_text(text)


