import json
from Config.config import MyLog

my_log = MyLog('MyLog', 'info').get_log()


# 以 Json 格式存储字典类型数据
def write_json_data(data):
    json_str = json.dumps(data, ensure_ascii=False, indent=4)
    txt_path = './OutPut/test_result.txt'
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(json_str)
        my_log.info("生成结果数据并储存在：{}".format(txt_path))
