# Playwright + Page Components

## 项目介绍
本项目基于 [Playwright](https://playwright.dev/) 进行端到端（E2E）测试，采用 **Page Components** 模式组织测试代码，提高可维护性和复用性。该模式通过将页面元素和交互封装为独立组件，使测试更加清晰、模块化。

## 安装与配置

### 1. 克隆项目
```sh
git clone <your-repository-url>
cd <your-project-folder>
```

### 2. 安装依赖
```sh
pip install playwright
```

### 3. 配置 Playwright
初始化 Playwright 配置（如果尚未配置）：
```sh
playwright install
```

## 运行测试

### 1. 运行所有测试
```sh
pytest Tests/
```

### 2. 运行特定测试
```sh
pytest Tests/test_login.py
```

### 3. 生成测试报告
```sh
pytest --html=report.html
```
然后在浏览器中打开 `report.html` 查看测试报告。

## 目录结构
```
project/
├── pages/                   # 页面层
│   ├── login_page.py        # 登录页面
│   └── 
├── components/              # 组件层
│   ├── base_component.py    # 组件基类
│   ├── login_form_component.py  # 登录表单组件
│   ├── 
│   └── 
├── tests/                   # 测试用例层
│   ├── test_login.py        # 登录测试
│   └── 
├── conftest.py              # Playwright 配置
├── requirements.txt         # Python 依赖
└── README.md                # 项目文档
```

## Page Components 说明
Page Components 采用 **面向对象封装**，每个页面组件提供特定的交互方法，例如：

```python
# Pages/login_page.py
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto('https://***.com/login')

    def login(self, username: str, password: str):
        self.page.fill('#username', username)
        self.page.fill('#password', password)
        self.page.click('button[type="submit"]')
```

## 贡献指南
欢迎提交 Issue 和 Pull Request 来改进本项目！

## 许可证
本项目基于 MIT 许可证开源。

