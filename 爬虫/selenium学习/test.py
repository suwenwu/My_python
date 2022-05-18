from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client

web = Chrome()

web.get('https://lms.ouchn.cn')

web.implicitly_wait(10)

img = web.find_element(By.XPATH, '//*[@id="kaptchaImage"]').screenshot_as_png
chaojiying = Chaojiying_Client('19855024955', 'sww0301..', '933372')
dic = chaojiying.PostPic(img, 1902)
verify_code = dic['pic_str']

web.find_element(By.XPATH, '//*[@id="loginName"]').send_keys('2232101200016')
web.find_element(By.XPATH, '//*[@id="password"]').send_keys('Ouchn@2021')
web.find_element(By.XPATH, '//*[@id="validateCode"]').send_keys(verify_code)
web.find_element(By.XPATH, '//*[@id="button"]').click()

windows = web.window_handles
web.switch_to.window(windows[0])

print(web.title)
