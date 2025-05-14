import requests
import time

url = "https://api-go.customeow.io/api/v1/picture-process/create"

start = time.time()
response = requests.get(url)
end = time.time()

print(f"状态码: {response.status_code}")
print(f"响应时间: {(end - start)*1000:.2f} ms")
