from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# 设置 Chrome 选项
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Program Files\chrome_114.0.5735.199\chrome.exe"  # Chrome 浏览器路径

# 指定 ChromeDriver 的路径
driver_path = r"C:\Program Files\chrome_114.0.5735.199\chrome.exe"  # 替换为你的 chromedriver 路径
service = Service(driver_path)

# 初始化 driver
driver = webdriver.Chrome(service=service, options=chrome_options)

# 打开初始页面
driver.get("https://uat-process-admin.maiyuan.online/#/task")

# 等待页面加载
time.sleep(2)

# 使用 JavaScript 注入 token
token = "your_token_here"  # 替换为你的 token
driver.execute_script(f"localStorage.setItem('token', '{token}');")  # 假设你的应用从 localStorage 获取 token

# 继续进行其他操作
