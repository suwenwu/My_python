from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# chrome_options = webdriver.ChromeOptions()
# # 使用代理
# proxy = '120.42.46.226:6666'
# chrome_options.add_argument('--proxy-server=%s' % proxy)
# web = Chrome(options=chrome_options)
web = Chrome()
# 进入58
web.get('https://zj.58.com/')

# 点击全职按钮
web.find_element(By.XPATH, '//*[@id="zpNav"]/em/a[1]').click()
time.sleep(3)

# 当前打开的所有窗口
windows = web.window_handles
# 转换到最新打开的窗口
web.switch_to.window(windows[-1])

# print(web.current_url)
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/ul[2]/li[16]/a').click()
li_list = web.find_elements(By.XPATH, '//*[@id="list_con"]/li')
for li in li_list:
    jobname = li.find_element(By.XPATH, './/span[@class="name"]').text
    jobprice = li.find_element(By.XPATH, './/p[@class="job_salary"]').text
    comp_name = li.find_element(By.XPATH, './div[2]/div/a').text

    print(jobname, jobprice, comp_name)
