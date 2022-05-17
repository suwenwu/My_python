import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import requests

web = Chrome()
url = 'http://quotes.toscrape.com/'
web.implicitly_wait(5)
web.get(url)
web.find_element(By.LINK_TEXT, 'Login').click()
windows = web.window_handles
web.switch_to.window(windows[0])

web.find_element(By.XPATH, '//*[@id="username"]').send_keys('admin')
web.find_element(By.XPATH, '//*[@id="password"]').send_keys('admin')
web.find_element(By.XPATH, '//input[@type="submit"]').click()

web.switch_to.window(windows[0])
time.sleep(1)
# 获取并处理cookies
cookies = {}
for data in web.get_cookies():
    cookies[data['name']] = data['value']
web.quit()

# 使用requests请求
resp = requests.get(url, cookies=cookies)
print(resp.text)
