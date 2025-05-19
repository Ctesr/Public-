

import requests

# 基础URL
BASE_URL = "https://sunzi-cool.staticmeow.com/product/customizer/json/shopline-{NUMBER}.json"


def read_ids_from_file(file_path):
    # 尝试常见编码
    encodings = ['utf-8', 'gbk', 'latin1', 'ISO-8859-1']

    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                ids = [line.strip() for line in file if line.strip()]
            print(f"成功使用编码: {encoding}")
            return ids
        except UnicodeDecodeError:
            print(f"编码 {encoding} 无效，尝试下一个编码...")

    raise ValueError("无法找到正确的文件编码")


# 检测URL是否存在
def check_urls(ids):
    """
    遍历ID列表，拼接URL并检测响应状态码
    """
    for num in ids:
        url = BASE_URL.format(NUMBER=num)
        response = requests.get(url)

        if response.status_code == 200:
            print(f"URL {url} returned 200: OK")
        elif response.status_code == 404:
            print(f"URL {url} returned 404: 没数据")
        else:
            print(f"URL {url} returned {response.status_code}: 其他原因")


# 主函数
def main():
    # 文件路径（假设文件名为ids.txt）
    file_path = 'D:\JCtestgit\Dome_project\新建 XLS 工作表.xls'

    # 读取ID
    ids = read_ids_from_file(file_path)
    print(f"读取到的ID列表: {ids}")

    # 检测URL
    check_urls(ids)


# 运行主函数
if __name__ == "__main__":
    main()