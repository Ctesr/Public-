import time
from playwright.async_api import Page, TimeoutError
from Config.config import MyLog

# 日志初始化
my_log = MyLog('MyLog', 'info').get_log()


class PlaywrightBasePageAsync:
    """
    基于 Playwright 的异步基础操作封装类
    """

    def __init__(self, page: Page):
        self.page = page  # Playwright Page 实例
        self.timeout = 15000  # 默认超时时间（单位：毫秒）

    async def find_ele(self, selector: str, ele_name='元素'):
        """
        等待并查找单个元素
        :param selector: CSS 选择器
        :param ele_name: 元素名称，用于日志记录
        :return: 定位到的 Locator 对象
        """
        my_log.info(f'开始在 {self.timeout / 1000} 秒内查找“{ele_name}”...')
        try:
            await self.page.wait_for_selector(selector, timeout=self.timeout)
            my_log.info(f'已查找到“{ele_name}”！')
            return self.page.locator(selector)
        except TimeoutError:
            my_log.error(f'查找“{ele_name}”失败，超时未找到！')
            raise

    async def find_eles(self, selector: str, ele_name='元素组'):
        """
        查找一组元素
        :param selector: CSS 选择器
        :param ele_name: 元素组名称
        :return: 定位到的 Locator 列表
        """
        my_log.info(f'开始查找一组“{ele_name}”...')
        try:
            await self.page.wait_for_selector(selector, timeout=self.timeout)
            my_log.info(f'已查找到“{ele_name}”！')
            return self.page.locator(selector)
        except TimeoutError:
            my_log.error(f'查找“{ele_name}”失败，超时未找到！')
            raise

    async def click(self, selector: str, ele_name='元素'):
        """
        点击元素
        :param selector: CSS 选择器
        :param ele_name: 元素名称
        """
        ele = await self.find_ele(selector, ele_name)
        await ele.click()
        my_log.info(f'点击“{ele_name}”')

    async def input(self, selector: str, text: str, ele_name='输入框'):
        """
        输入文本
        :param selector: CSS 选择器
        :param text: 输入内容
        :param ele_name: 元素名称
        """
        ele = await self.find_ele(selector, ele_name)
        await ele.fill(text)
        my_log.info(f'在“{ele_name}”中输入“{text}”')

    async def js_execute_input(self, selector: str, text: str, ele_name='输入框'):
        """
        使用 JS 设置输入框的 value 值
        :param selector: CSS 选择器
        :param text: 输入内容
        :param ele_name: 元素名称
        """
        script = f'document.querySelector("{selector}").value="{text}";'
        await self.page.evaluate(script)
        my_log.info(f'对“{ele_name}”执行 JS 输入 "{text}"')

    async def js_execute_style(self, selector: str, ele_name='元素'):
        """
        使用 JS 修改元素样式
        :param selector: CSS 选择器
        :param ele_name: 元素名称
        """
        script = f'document.querySelector("{selector}").style.cursor="pointer";'
        await self.page.evaluate(script)
        my_log.info(f'对“{ele_name}”执行 JS 修改样式')

    async def get_text(self, selector: str, ele_name='元素'):
        """
        获取元素文本内容
        :param selector: CSS 选择器
        :param ele_name: 元素名称
        :return: 文本内容
        """
        ele = await self.find_ele(selector, ele_name)
        text = await ele.text_content()
        my_log.info(f'获取“{ele_name}”的文本：{text}')
        return text

    async def get_attribute(self, selector: str, attr_name: str, ele_name='元素'):
        """
        获取元素属性值
        :param selector: CSS 选择器
        :param attr_name: 属性名称
        :param ele_name: 元素名称
        :return: 属性值
        """
        ele = await self.find_ele(selector, ele_name)
        attr = await ele.get_attribute(attr_name)
        my_log.info(f'获取“{ele_name}”的属性“{attr_name}”：{attr}')
        return attr

    async def get_url(self):
        """
        获取当前页面 URL
        :return: 页面 URL
        """
        url = self.page.url
        my_log.info(f'获取当前页面 URL：{url}')
        return url

    async def get_title(self):
        """
        获取当前页面标题
        :return: 页面 Title
        """
        title = await self.page.title()
        my_log.info(f'获取当前页面标题：{title}')
        return title

    async def open_url(self, url: str):
        """
        打开指定 URL 页面
        :param url: 目标网址
        """
        await self.page.goto(url, timeout=self.timeout)
        my_log.info(f'打开页面：{url}')

    async def save_screenshot(self, name: str, img_path: str):
        """
        截图并保存到指定目录
        :param name: 用例名称
        :param img_path: 文件夹路径（相对于 Screenshot 根目录）
        """
        now_time = time.strftime("%Y%m%d%H%M%S")
        path = f"./OutPut/Screenshot/{img_path}/{name}_{now_time}.png"
        await self.page.screenshot(path=path)
        my_log.info(f'截取页面截图，保存至：{path}')
