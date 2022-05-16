import requests
# 忽略requests证书警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://ssr2.scrape.center/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
    # "Host": "www.douban.com",
}
resp = requests.get(url, headers=headers, verify=False)

print(resp.text)
