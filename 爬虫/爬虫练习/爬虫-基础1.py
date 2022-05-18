# import requests
# from lxml import etree
#
# url = 'http://www.glidedsky.com/level/web/crawler-basic-1'
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
#     "Cookie": "footprints=eyJpdiI6ImM4ZVl4SHg3ZnhDNFU1OE9CZFk3YWc9PSIsInZhbHVlIjoiNTNoRFwvTStQdjdZTVBjZVNhSnFYekw4dUZHbU9xeW96bHZ1bHZQTTJZWDBDd3dUblgyWGFMRktZa09rWkEza2ciLCJtYWMiOiJmMzY3YzRjMzJkYzUwYzUyOTQ2NjQwNmY1N2IwMDFmZTgzMzY3MTE4NzA4ZTJkZjQ4ZjRkYTYyZDVlMTE4Y2ZjIn0=; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6Ind0VkhDb3JuMVFUdFQrNGY0UzNwYlE9PSIsInZhbHVlIjoiZHFuSndKTExSaDlvTk84SUMzZFwvTDYzQmZSUnVVV3lnK05aOWhBS3FCYWtJdXBYQ0Z0eVwvcThFaUxtUUhEQ01LOXRVdCt2UkJqRHhqdFZLK0VjZENhdlwvYVIzR3Y0Z05QSzJxTzk3blp6QTdtYkJpakxcL0E5ZkRCWGJaRmVjanFaXC9GOXdidVRtM0cxRFhsaDdzTXZ6MWQyTUdEWnNzN28rV2VoaHVrdTZCRVk9IiwibWFjIjoiOTgzODdlZmMwNmJmNDgyMmMxNjUzNWE2ZDgxMTAzNDQyYWI1MGE1Yzg5NDcxY2QwYTA1ZjQ5YzNiNDQwNmMwZSJ9; XSRF-TOKEN=eyJpdiI6IkNIQnpUemZqZHJDTGhQYzd1MUxkXC9RPT0iLCJ2YWx1ZSI6Ikh0aVlDSUZWMWsyR2RvdGg4RkJETW9MR3d0MDJWdk1xam1NMkJjSXIycTZ4UFJZWmZrXC9lKzZreW1MWmo4cHhwIiwibWFjIjoiNmU2MWU3ZmQ5NTdjOTU5MGYzOWUxYTdhMmEwYWY5NzQ5NGM3MGZiYzNjM2Q3YWU2NTNmNTBiYmYzMzRhNjdkMiJ9; glidedsky_session=eyJpdiI6IjdWQnJ1SmxPaXBibVYra0tvQWhKTGc9PSIsInZhbHVlIjoiWVNWNnJEazA4b3FmSDJaN2tSYVdPUUxMNXI4Qm5WMU5KNVwvVXBVQU01NFdJdkwwNnZGaVJPRzZoSU9nKzV6TzEiLCJtYWMiOiJjZmIyOTJkOTNkMDExOTE0OWE0ZDI0NGVhZTQ0MDc2ZmFjYjFiNWNiZjE3ODJjZjQ0NmMxM2JlY2ZmM2Y0OGFjIn0="
# }
# resp = requests.get(url, headers=headers)
#
# page = etree.HTML(resp.content)
# nums = page.xpath('//div[@class="col-md-1"]/text()')
# sum = 0
# for i in nums:
#     sum += int(i)
# print(sum)
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

url = 'http://www.glidedsky.com/login'

web = Chrome()

web.get(url)

web.find_element(By.CSS_SELECTOR, '#email').send_keys('418160668@qq.com')
web.find_element(By.CSS_SELECTOR, '#password').send_keys('sww0301..')
web.find_element(By.XPATH, '//button[@type="submit"]').click()

time.sleep(1)

windows = web.window_handles

web.switch_to.window(windows[0])

time.sleep(1)

web.find_element(By.LINK_TEXT, '爬虫-基础1').click()

web.switch_to.window(windows[0])

web.find_element(By.LINK_TEXT, '待爬取网站').click()

windows = web.window_handles
web.switch_to.window(windows[1])

# 进行累加求和
time.sleep(1)
num_list = web.find_elements(By.XPATH, '//*[@id="app"]/main/div[1]/div/div/div/div')
ans = 0
for num in num_list:
    ans += int(num.text)

web.switch_to.window(windows[0])
time.sleep(1)
answer = web.find_element(By.XPATH, '//*[@id="app"]/main/div[1]/div/div/form/div/input[1]')
answer.clear()
answer.send_keys(ans)

web.find_element(By.XPATH, '//button[@type="submit"]').click()

web.quit()
