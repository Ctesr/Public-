import json


# 读取 Json 测试数据
def read_json_data(filename):
    with open("./TestDatas/Json/" + filename, "r", encoding="utf-8") as f:
        list_data = []
        dict_data = json.load(f)
        for value in dict_data.values():
            list_data.append(value)
        return list_data


# 读取 Json list 测试数据
def read_json_list(filename):
    with open("./TestDatas/Json/" + filename, "r", encoding="utf-8") as f:
        dict_data = json.load(f)
        return dict_data
