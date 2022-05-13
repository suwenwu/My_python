import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.keys import Keys

web = Chrome()
web.get('https://www.chaojiying.com/user/login/')
time.sleep(1)

# 识别验证码
img = web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('19855024955', 'sww0301..', '933372')
dic = chaojiying.PostPic(img, 1902)
verify_code = dic['pic_str']

# 输入用户名，密码，验证码
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('19855024955')
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('sww0301..')
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)

# 点击登陆
submit = web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input')
submit.click()
time.sleep(5)
print(web.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]').text)
