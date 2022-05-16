import requests
from requests.auth import HTTPBasicAuth

url = 'https://ssr3.scrape.center/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
    # "Host": "www.douban.com",
}
auth = HTTPBasicAuth('admin', 'admin')
resp = requests.get(url, headers=headers, auth=auth)

print(resp.text)
