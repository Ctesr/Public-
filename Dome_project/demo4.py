from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 配置代理参数
    proxy_settings = {
        "server": "http://127.0.0.1:7897",  # 代理地址和端口
        # "username": "fang33847261@gmail.com",  # 代理认证用户名（可选）
        # "password": "Fang33847261"  # 代理认证密码（可选）
    }

    # 启动浏览器并应用代理
    browser = p.chromium.launch(proxy=proxy_settings)

    # 创建页面并访问网站
    page = browser.new_page()
    page.goto("https://giftlab.com/products/photo-blanket-fleece-blanket-best-gift-for-grandpa")
    print("访问")



    #
    # print(page.content())