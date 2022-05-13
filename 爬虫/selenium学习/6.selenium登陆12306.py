import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

# chrome版本88之前
# web = Chrome()
# web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#             "source": """
#                                         Object.defineProperty(navigator, 'webdriver', {
#                                             get: () => undefined
#                                         });
#                                     """
#         })

# chrome版本88之后

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("disable-blink-features=AutomationControlled")  # 就是这一行告诉chrome去掉了webdriver痕迹
web = Chrome(options=chrome_options)

web.get('https://kyfw.12306.cn/otn/resources/login.html')

time.sleep(1)

# 输入账号密码，点击登陆
web.find_element(By.XPATH, '//*[@id="J-userName"]').send_keys('123456789')
web.find_element(By.XPATH, '//*[@id="J-password"]').send_keys('123456789')
web.find_element(By.XPATH, '//*[@id="J-login"]').click()

time.sleep(3)

# 滑块验证
btn = web.find_element(By.XPATH, '//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(btn, 310, 0).perform()
