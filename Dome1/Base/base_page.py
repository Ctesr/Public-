import os
import time
# from Config.config import MyLog

# my_log = MyLog('MyLog', 'info').get_log()

""" 二次封装selenium方法 """


class BasePageAction:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 25  # 显示等待超时时间
        self.poll_frequency = 0.5  # 轮询频率

    def find_ele(self, element, ele_name='元素'):
        """ 定位元素基础方法
        :param element: 要定位的元素，以元组的形式(定位方式, 属性值)，如：(By.ID, 'name')
        :param ele_name: 元素名称
        :return: 定位到的元素
        """
        try:
            time.sleep(1)
            # my_log.info('开始在{}秒内查找“{}”., {}..'.format(self.timeout, ele_name, element))
            WebDriverWait(self.driver, self.timeout, self.poll_frequency) \
                .until(lambda x: x.find_element(*element))
            # my_log.info('已查找到“{}”！'.format(ele_name))
            ele = self.driver.find_element(*element)
            # my_log.info('已查找到元素的text“{}”！'.format(ele.text))
            return ele
        except TimeoutException:
            # my_log.error('未能在指定时间内找到“{}”！'.format(ele_name))
            raise

    def find_eles(self, element, ele_name):
        """ 定位一组元素基础方法
        :param element: 要定位的元素，以元组的形式(定位方式, 属性值)，如：(By.ID, 'name')
        :param ele_name: 元素名称
        :return: 定位到的一组元素
        """
        # my_log.info('开始在{}秒内查找“{}”...'.format(self.timeout, ele_name))
        WebDriverWait(self.driver, self.timeout, self.poll_frequency) \
            .until(lambda x: x.find_elements(*element))
        # my_log.info('已查找到“{}”！'.format(ele_name))
        return self.driver.find_elements(*element)

    """--------------------对元素进行操作--------------------"""

    def js_execute_input(self, text, element, ele_name):
        """ 执行js语句输入文本
        :param text: 输入的文本内容
        :param element: 要定位的元素，以元组的形式(定位方式, 属性值)，如：(By.ID, 'name')
        :param ele_name: 元素名称
        :return:
        """
        self.driver.execute_script('arguments[0].setAttribute("value","{}")'.format(text),
                                   self.find_ele(element, ele_name))
        # my_log.info('对“{}”执行js语句输入文本'.format(ele_name))

    def js_del(self, element, ele_name):
        """ 执行js语句删除元素
        :param element: 要定位的元素，以元组的形式(定位方式, 属性值)，如：(By.ID, 'name')
        :param ele_name: 元素名称
        :return:
        """
        element = self.find_ele(element, ele_name)
        self.driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element)
        # my_log.info('删除“{}”的元素'.format(ele_name))

    def js_dels(self, element, index, ele_name):
        """ 执行js语句删除元素
        :param element: 要定位的元素，以元组的形式(定位方式, 属性值)，如：(By.ID, 'name')
        :param index: 定位到元素列表的下标
        :param ele_name: 元素名称
        :return:
        """
        element = self.find_eles(element, ele_name)[index]
        self.driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element)
        # my_log.info('删除“{}”的元素'.format(ele_name))

    def js_execute_style(self, element, ele_name):
        """ 执行js语句修改元素样式
        :param element: 要定位的元素，以元组的形式(定位方式, 属性值)，如：(By.ID, 'name')
        :param ele_name: 元素名称
        :return:
        """
        self.driver.execute_script('arguments[0].setAttribute("style",arguments[1])', self.find_ele(element, ele_name),
                                   "cursor: pointer !important;")
        # self.driver.execute_script('arguments[0].setAttribute("class","jsx-89fc9ad378f03748 p-3.5 text-green-7 hover:text-green-8 cursor-pointer")', self.find_ele(element, ele_name))
        # my_log.info('对“{}”执行js语句修改元素样式'.format(ele_name))

    def click(self, element, ele_name):
        """ 点击
        :param element: 要定位的元素，以元组的形式(定位方式, 属性值)，如：(By.ID, 'name')
        :param ele_name: 元素名称
        :return:
        """
        self.find_ele(element, ele_name).click()
        # my_log.info('点击“{}”'.format(ele_name))

    def clicks(self, element, index, ele_name):
        """ 点击
        :param element: 要定位的元素，以元组的形式(定位方式, 属性值)，如：(By.ID, 'name')
        :param index: 定位到元素列表的下标
        :param ele_name: 元素名称
        :return:
        """
        self.find_eles(element, ele_name)[index].click()
        # my_log.info('点击“{}”'.format(ele_name))

    def double_click_input(self, element, text, ele_name):
        """ 双击输入
        :param element: 要定位的元素，以元组的形式(定位方式, 属性值)，如：(By.ID, 'name')
        :param text: 输入的文本内容
        :param ele_name: 元素名称
        :return: 无
        """
        ele = self.find_ele(element, ele_name)
        ActionChains(self.driver).double_click(ele).perform()
        ele.send_keys(text)
        # my_log.info('双击“{0}”的内容，在“{0}”内输入 “{1}”'.format(ele_name, text))

    def mouse_click(self, element, ele_name):
        """ 鼠标点击
        :param element: 要定位的元素，以元组的形式(定位方式, 属性值)，如：(By.ID, 'name')
        :param ele_name: 元素名称
        :return: 无
        """
        ele = self.find_ele(element, ele_name)
        ActionChains(self.driver).click(ele).perform()
        # my_log.info('点击“{}”'.format(ele_name))

    def mouse_clicks(self, element, index, ele_name):
        """ 鼠标点击
        :param element: 要定位的元素，以元组的形式(定位方式, 属性值)，如：(By.ID, 'name')
        :param index: 定位到元素列表的下标
        :param ele_name: 元素名称
        :return: 无
        """
        ele = self.find_eles(element, ele_name)[index]
        ActionChains(self.driver).click(ele).perform()
        # my_log.info('点击“{}”'.format(ele_name))

    def input(self, element, text, ele_name):
        """ 点击输入
        :param element: 要定位的元素，以元组的形式(定位方式, 属性值)，如：(By.ID, 'name')
        :param text: 输入的文本内容
        :param ele_name: 元素名称
        :return: 无
        """
        self.find_ele(element, ele_name).send_keys(text)
        # my_log.info('点击“{0}”的内容，在“{0}”内输入 “{1}”'.format(ele_name, text))

    def inputs(self, element, index, text, ele_name):
        """ 点击输入
        :param element: 要定位的元素，以元组的形式(定位方式, 属性值)，如：(By.ID, 'name')
        :param index: 定位到元素列表的下标
        :param text: 输入的文本内容
        :param ele_name: 元素名称
        :return: 无
        """
        self.find_eles(element, ele_name)[index].send_keys(text)
        # my_log.info('点击“{0}”的内容，在“{0}”内输入 “{1}”'.format(ele_name, text))

    def clear_input(self, element, text, ele_name):
        """ 清除并输入
        :param element: 要定位的元素，以元组的形式(定位方式, 属性值)，如：(By.ID, 'name')
        :param text: 输入的文本内容
        :param ele_name: 元素名称
        :return: 无
        """
        self.find_ele(element, ele_name).send_keys(Keys.CONTROL, 'a')  # 使用键盘全选
        self.find_ele(element, ele_name).send_keys(text)  # 输入内容实现清除文本并输入
        # my_log.info('清除“{0}”的内容，在“{0}”内输入 “{1}”'.format(ele_name, text))

    def clear(self, element, ele_name):
        """
        清除输入框
        """
        self.find_ele(element, ele_name).clear()
        # my_log.info('清除"{}"的内容'.format(ele_name))

    def choose_drop_down_box(self, element, text, ele_name):
        """ 下拉选择
        :param element: 要定位的元素，以元组的形式(定位方式, 属性值)，如：(By.ID, 'name')
        :param text: 选择的文本内容
        :param ele_name: 元素名称
        :return: 无
        """
        Select(self.find_ele(element, ele_name)).select_by_visible_text(text)
        # my_log.info('在“{0}”内选择 “{1}”'.format(ele_name, text))

    """-----------------------------------------------------"""

    """--------------------对浏览器进行操作--------------------"""

    def get_url(self):
        """
        获取页面URL
        @return: 当前页面URL地址
        """
        # my_log.info('获取当前打开窗口页面的URL')
        return self.driver.current_url

    def get_title(self):
        """
        获取页面Title
        @return: 当前页面Title文本
        """
        # my_log.info('获取当前打开窗口页面的Title')
        return self.driver.title

    def open_url(self, url):
        """
        打开页面URL
        """
        # self.driver.set_page_load_timeout(120)  # 设置页面加载超时时间为10秒
        self.driver.get(url)
        # my_log.info('打开{}页面'.format(url))

    def open_new_page(self, url):
        """
        打开新的页面URL
        """
        self.driver.execute_script(f"window.open('{url}');")
        # my_log.info('在新的窗口中打开{}页面'.format(url))

    def refresh_page(self):
        """
        刷新当前页面
        """
        self.driver.refresh()
        # my_log.info('刷新页面')

    def js_execute_home(self):
        """
        执行js语句滚动到页面顶部
        """
        self.driver.execute_script('window.scrollTo(0, 0);')
        # my_log.info('滚动到页面顶部')

    def js_execute_end(self):
        """
        执行js语句滚动到页面底部
        """
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        # my_log.info('滚动到页面底部')

    """-----------------------------------------------------"""

    """--------------------获取元素信息--------------------"""

    def get_size(self, element, ele_name):  # 获取元素大小
        ele = self.find_ele(element, ele_name)
        # my_log.info('获取“{}”元素的大小...'.format(ele_name))
        return ele.size

    def get_text(self, element, ele_name):  # 获取文本
        ele = self.find_ele(element, ele_name)
        # my_log.info('获取“{}”元素的文本...'.format(ele_name))
        return ele.text

    def get_texts(self, element, index, ele_name):  # 获取文本
        ele = self.find_eles(element, ele_name)
        # my_log.info('获取“{}”元素的文本...'.format(ele_name))
        return ele[index].text

    def get_attributes(self, element, name, ele_name):  # 获取元素属性
        ele = self.find_ele(element, ele_name)
        # my_log.info('获取“{}”元素的“{}”属性...'.format(ele_name, name))
        return ele.get_attribute(name)

    def whether_select(self, element, ele_name):  # 判断是否被选中
        ele = self.find_ele(element, ele_name)
        # my_log.info('判断“{}”元素是否选中...'.format(ele_name))
        return ele.is_selected()

    def whether_enabled(self, element, ele_name):  # 判断是否可用
        ele = self.find_ele(element, ele_name)
        # my_log.info('判断“{}”元素是否可用...'.format(ele_name))
        return ele.is_enabled()

    def whether_displayed(self, element, ele_name):  # 判断是否可见
        ele = self.find_ele(element, ele_name)
        # my_log.info('判断“{}”元素是否可见...'.format(ele_name))
        return ele.is_displayed()

    def is_ele_exist(self, element, ele_name):  # 判断是否存在
        try:
            self.driver.find_element(*element)
            # my_log.info('判断“{}”元素是否存在...'.format(ele_name))
            return True
        except:
            return False

    """-----------------------------------------------------"""

    """--------------------切换frame操作--------------------"""

    def switch_to_frame(self, frame_element, ele_name='页面frame'):
        """ 切换frame
        :param frame_element: 要定位的元素，以元组的形式(定位方式, 属性值)，如：(By.ID, 'name')
        :param ele_name: 元素名称，默认为‘页面frame’
        :return: 无
        """
        self.driver.switch_to.frame(self.find_ele(frame_element, ele_name))
        # my_log.info('切换至{}...'.format(ele_name))

    def switch_to_default(self):
        """ 切换回默认frame
        :return: 无
        """
        # my_log.info('切换回默认位置...')
        self.driver.switch_to.default_content()

    """-----------------------------------------------------"""

    """--------------------切换窗口操作--------------------"""

    def switch_windows(self, wind_handle):
        """ 切换窗口
        :param wind_handle: 需要切换的第n个窗口
        :return: 无
        """
        handles = self.driver.window_handles
        # my_log.info('获取当前打开的所有窗口handle...')
        self.driver.switch_to.window(handles[wind_handle])
        # my_log.info('切换到第{}个窗口'.format(wind_handle))

    """-----------------------------------------------------"""

    def auto_create_dir(self, path):
        """ 自动创建目录
        :param path: 需要自动创建文件夹的路径
        :return: 无
        """
        if not os.path.exists(path):
            os.makedirs(path)
            # my_log.info('检查到没有输出的目录，正在创建...')

    """-----------------------------------------------------"""

    def save_page_screenshot(self, name, img_path):
        """ 保存截图
        :param name: 用例名称
        :param img_path: 保存到Screenshot下的文件夹路径
        :return: 无
        """
        screenshots_path = f"./OutPut/Screenshot/{img_path}"
        self.auto_create_dir(screenshots_path)
        now_time = time.strftime("%Y%m%d%H%M%S")
        output_path = screenshots_path + f'/{name}_{now_time}.png'
        self.driver.get_screenshot_as_file(output_path)
        # my_log.info('截取当前页面并存储在：{}'.format(output_path))

    """-----------------------------------------------------"""

    def save_page(self, name, page_path):
        """ 保存当前网页内容
        :param name: 用例名称
        :param page_path: 保存到OutPut下的文件夹路径
        :return: 无
        """
        now_time = time.strftime("%Y%m%d%H%M%S")
        output_path = f"./OutPut/{page_path}"
        self.auto_create_dir(output_path)
        save_path = f"{output_path}/{name}_{now_time}.html"
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)
            # my_log.info('存储当前页面内容在：{}'.format(save_path))
