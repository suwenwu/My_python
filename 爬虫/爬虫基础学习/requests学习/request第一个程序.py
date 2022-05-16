import requests

url = 'https://www.baidu.com/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3880.400 QQBrowser/10.8.4554.400"
}
resp = requests.get(url, headers=headers)
# 打印响应页面的编码格式
print(resp.apparent_encoding)
# 打印请求url
print(resp.url)
# 打印响应状态码
print(resp.status_code)
# 打印响应文本信息
print(resp.text)
