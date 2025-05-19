import requests
from lxml import html
import time
import json

env = "beta"
admin_token = ""


class CustoMeowAPI:
    def __init__(self):
        self.dev_token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mzc2MTIxNjAsInN1YiI6IjM3ODY0OTA0MzIwOTA5MzEyIn0.TeCqokjTd-n_eTPhOTd36UDg7ehvedSf_R6q4uuTZnE"
        self.beta_token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDYzMjIwODYsInN1YiI6IjM3ODY0OTA0MzIwOTA5MzEyIn0.eFU0-HxKZGiDnSd9D_Ip7jEHJvYuYOw9yzlXa07oXlo"
        self.uat_token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDEzMjk2MjUsInN1YiI6IjQxNTM3OTQ3NDA0NjA3NDg4In0.93Pdem-ushLYWKcsygjM2nrQl_f2AoKQFtodHmOwvrs"

    def get_header(self, env):
        admin_token = ""
        if env == "beta":
            admin_token = self.beta_token
        elif env == "uat":
            admin_token = self.uat_token
        elif env == "dev":
            admin_token = self.dev_token
        else:
            raise ValueError("Invalid environment. Please input 'beta' or 'uat' or 'dev'.")
        headers = {
            "User-Agent": "Apifox/1.0.0 (https://apifox.com)",
            "Content-Type": "application/json",
            "Authorization": f"{admin_token}",
            "Accept": "*/*",
            "Host": f"api-go-{env}-customeow.maiyuan.online",
            "Connection": "keep-alive"
        }
        return headers

    def get_uid(self, env, user_email):
        url = f"https://api-go-{env}-customeow.maiyuan.online/admin/v1/user/users?page=1&pageSize=100&orderBy=createdAt&sortBy=desc&userKind=0&keyword={user_email}"  # 替换为您要请求的实际URL
        headers = self.get_header(env)
        response = requests.get(url, headers=headers)
        print("Status Code:", response.status_code)
        print("Response Data:", response.json())
        uid = response.json()['data']['list'][0]['id']
        print(f"userid: {uid}")
        return uid

    def api_3sum(self, env, hour, sum_count=1):
        url = f"https://api-go-{env}-customeow.maiyuan.online/admin/v1/third-service/force-handle-cache-data"
        headers = self.get_header(env)
        data = {
            "hour": hour,
        }
        for i in range(sum_count):
            time.sleep(1)
            response = requests.post(url, data=data, headers=headers)
            print("Status Code:", response.status_code)
            print("Response Data:", response.text)

    def reset_14(self, env, user_email):  # 不要线上使用
        # 请求地址和路径
        url = f"https://api-go-{env}-customeow.maiyuan.online/admin/v1/subscription/user-subscription/reset"
        headers = self.get_header(env)
        # 请求数据
        data = {
            "email": user_email,
        }

        # 发送POST请求
        response = requests.post(url, headers=headers, json=data)

        # 打印响应结果
        print("Status Code:", response.status_code)
        print("Response Data:", response.json())

    def change_subscription(self, env, uid, startAt, endAt):
        url = f"https://api-go-{env}-customeow.maiyuan.online/admin/v1/subscription/user-subscription/change-subscription"
        headers = self.get_header(env)
        data = {
            "userId": uid,
            "subscriptionType": 1,  # 1=free 2=订阅
            "startAt": startAt,
            "endAt": endAt,
            # "subscriptionIsAutoRenew": 1  # 0=不续订， 1=续订
        }
        response = requests.post(url, json=data, headers=headers)
        print("Status Code:", response.status_code)
        print("Response Data:", response.json())

    # 重置积分的接口
    def change_credits(self, env, email):
        url = f'https://api-go-{env}-customeow.maiyuan.online/admin/v1/user/user-credits/reset'
        headers = self.get_header(env)
        data = {
            "email": email
        }
        response = requests.post(url, headers=headers, json=data)
        print(response)
        print("重置积分的接口 Code:", response.status_code)
        print("重置积分的接口Response Data:", response.json())

    def change_vip_endAt(self, env):
        url = "https://api-go-uat-customeow.maiyuan.online/admin/v1/subscription/user-subscription/vip-update"
        headers = self.get_header(env)
        data = {
            "Id": 37867237226319872,  # vip id
            "endAt": "2024-08-01T15:33:40+08:00"
        }
        response = requests.post(url, json=data, headers=headers)
        print("Status Code:", response.status_code)
        print("Response Data:", response.json())

    def change_subEndAt(self, env, email, EndAt):
        # 请求地址和路径
        url = f'https://api-go-{env}-customeow.maiyuan.online/admin/v1/subscription/user-subscription/update-time'
        headers = self.get_header(env)
        # 请求数据
        data = {
            "email": email,
            "subscriptionEndAt": EndAt
        }
        # 发送POST请求
        response = requests.post(url, headers=headers, json=data)
        # 打印响应结果
        print("Status Code:", response.status_code)
        print("Response Data:", response.json())


class ApiReference:
    def __init__(self):
        self.lang_list = ['en_US', 'de_DE', 'fr_FR', 'pt_BR', 'es_ES', 'ja_JP', 'it_IT', 'nl_NL', 'zh_TW', 'zh_CN', 'he_IL',
                          'ru_RU', 'ar_AR', 'th_TH', 'id_ID', 'tr_TR', 'vi_VI', 'sv_SV', 'pl_PL', 'pt_PT', 'ko_KR', 'el_GR', 'cs_CZ', 'ro_RO', 'sk_SK', 'hu_HU', 'bg_BG']

    def get_api_key(self, env):
        domainName = ""
        headers = {}
        if env == "beta":
            domainName = "https://api-go-beta-customeow.maiyuan.online/open/"  # 域名
            headers = {"x-api-key": "15d91c255d6e4caf2d4cd0beb15837375aaca8fc"}  # Api令牌
        elif env == "uat":
            domainName = "https://api-go-uat-customeow.maiyuan.online/open/"
            headers = {"x-api-key": "6d2c848f7291c7aadce1808893461c590aee9b2b"}
        elif env == "prod":
            domainName = "https://openapi.customeow.io/"
            headers = {"x-api-key": "dd20727a0569900d7e3ed169f3f6a054c1867d41"}
        return domainName, headers


    def get_order_list_V1(self, env, page=None, pageSize=None):
        domainName, headers = self.get_api_key(env)
        url = f"{domainName}v1/order?page={page}&pageSize={pageSize}"
        # 发送GET请求
        response = requests.get(url, headers=headers)
        # 打印响应结果
        result = {
            "TestName": "get_order_list_V1",
            "Url": url,
            "StatusCode": response.status_code,
            "ResponseData": response.json(),
        }
        print(result)

    def get_order_V1(self, env, storeId="107530295472842304", platformOrderId="107530295472842366", lang="en_US"):
        domainName, headers = self.get_api_key(env)
        url = f"{domainName}v1/order-info?storeId={storeId}&platformOrderId={platformOrderId}&lang={lang}"
        # 发送GET请求
        response = requests.get(url, headers=headers)
        # 打印响应结果
        result = {
            "TestName": "get_order_V1",
            "Url": url,
            "StatusCode": response.status_code,
            "ResponseData": response.json(),
        }
        print(result)

    def get_custom_data_V1(self, env, customInfoId="53424155105734656", lang="en_US"):
        domainName, headers = self.get_api_key(env)
        url = f"{domainName}v1/custom-info/{customInfoId}?lang={lang}"
        # 发送GET请求
        response = requests.get(url, headers=headers)
        # 打印响应结果
        result = {
            "TestName": "get_custom_data_V1",
            "Url": url,
            "StatusCode": response.status_code,
            "ResponseData": response.json(),
        }
        print(result)

    def get_template_data_V1(self, env, customInfoId="53424155105734656", lang="en_US"):
        domainName, headers = self.get_api_key(env)
        url = f"{domainName}v1/custom-info/{customInfoId}/templates?lang={lang}"
        # 发送GET请求
        response = requests.get(url, headers=headers)
        # 打印响应结果
        result = {
            "TestName": "get_template_data_V1",
            "Url": url,
            "StatusCode": response.status_code,
            "ResponseData": response.json(),
        }
        print(result)

    def create_production_template_task_V1(self, env, customInfoId, compositeId):
        domainName, headers_key = self.get_api_key(env)
        # 请求头
        headers = {
            "Content-Type": "application/json",
            "x-api-key": headers_key["x-api-key"],
        }
        url = f"{domainName}v1/composite/task"
        data = {
            "customInfoId": customInfoId,
            "compositeId": compositeId,
        }
        print(headers, data)
        # 发送POST请求
        response = requests.post(url, headers=headers, json=data)
        # 打印响应结果
        result = {
            "TestName": "create_production_template_task_V1",
            "Url": url,
            "StatusCode": response.status_code,
            "ResponseData": response.json(),
        }
        print(result)

    def query_task_result_V1(self, env, tid="181483232296980480"):
        domainName, headers = self.get_api_key(env)
        url = f"{domainName}v1/composite/task/{tid}"
        # 发送GET请求
        response = requests.get(url, headers=headers)
        # 打印响应结果
        result = {
            "TestName": "query_task_result_V1",
            "Url": url,
            "StatusCode": response.status_code,
            "ResponseData": response.json(),
        }
        print(result)







if __name__ == "__main__":
    test = CustoMeowAPI()
    # result = test.get_header(env="uat")
    # print(result)

    """获取uid"""
    # uid = test.get_uid(env="beta", user_email="idd-home@idd.cool")
    """修改订阅→免费"""
    # test.change_subscription(env="beta", uid=uid, startAt="2024-11-01T00:00:00Z", endAt="2024-11-07T06:38:00Z")  # TODO 只改免费类型，改时间无用
    """修改订阅结束时间"""
    # test.change_subEndAt(env="beta", email="idd-home@idd.cool", EndAt=1734919200)
    # test.change_subEndAt(env="uat", email="liujinjie@idd.cool", EndAt=1737080160)
    """重置积分的接口"""
    # test.change_credits(env="beta", email="idd-home@idd.cool")
    test.change_credits(env="beta", email="fang33847261@gmail.com")
    """立刻统计三方调用"""
    # test.api_3sum(env="beta", hour="2025-03-06 01:00:00", sum_count=1)  # 当前时间-8
    # test.api_3sum(env="uat", hour="2025-03-06 09:00:00", sum_count=1)  # 当前时间-8
    """重置账号的试用期"""
    # test.reset_14(env="dev", user_email="idd-home@idd.cool")
    # test.reset_14(env="beta", user_email="liujinjie129@gmail.com")
    # test.reset_14(env="uat", user_email="liujinjie129@gmail.com")

    """重置账号"""
    # emails = [
    #     "zzj@idd.cool",
    #     "liujinjie@idd.cool",
    #     "liujinjie129@gmail.com",
    #     "xiangliuxp@gmail.com",
    #     "aa1291029266@icloud.com",
    #     "1291029266@qq.com",
    #     "1635376788@qq.com",
    #     "1803973712@qq.com",
    #     "liujinjie129@outlook.com"
    # ]
    # for i in emails:
    #     print(f"正在重置账号的积分和订阅：{i}")
    #     test.change_credits(env="uat", email=i)
    #     test.reset_14(env="uat", user_email=i)


    """API文档"""
    # apitest = ApiReference()
    """get_custom_data_V1"""
    # for i in lang_list:
    #     time.sleep(0.5)
    # apitest.get_custom_data_V1(env="beta", customInfoId="169819265384341504", lang='en_US')  # 169819265384341504, 53424155105734656, "测试"
    # get_custom_data_V1(env="uat", customInfoId='174175535537106944', lang='en_US')  # 174175535537106944, 53424155105734656, "测试"
    # get_custom_data_V1(env="prod", customInfoId='174898470304374784', lang='en_US')  # 174898470304374784, 53424155105734656, "测试"
    """get_template_data_V1"""
    # apitest.get_template_data_V1(env="beta", customInfoId="169819265384341504", lang='en_US')

    """get_order_list_V1"""
    # apitest.get_order_list_V1(env="beta", page=4, pageSize=3)
    """get_order_V1"""
    # apitest.get_order_V1(env="beta", storeId="140526201679642624", platformOrderId="5766420922582", lang="en_US")  # Shopify

    """create_production_template_task_V1"""
    # apitest.create_production_template_task_V1(env="beta", customInfoId="141121593085538304", compositeId="42196802438430720")
    """query_task_result_V1"""
    # apitest.query_task_result_V1(env="beta", tid="181483232296980480")

