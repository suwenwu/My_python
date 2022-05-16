import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disbale-gpu")

web = Chrome(options=opt)

url = 'https://www.baidu.com/'
web.get(url)

# 隐式等待
web.implicitly_wait(10)

# 通过id值来定位元素
# web.find_element(By.ID, 'kw').send_keys('python3')
# 通过css选择器来定位元素
# web.find_element(By.CSS_SELECTOR, '#kw').send_keys('python3')
# 通过xpath定位
# web.find_element(By.XPATH, '//input[@id="kw"]').send_keys('python3')
# 通过class属性来定位
# web.find_element(By.CLASS_NAME, 's_ipt').send_keys('python3')
# 通过name属性来定位
# web.find_element(By.NAME, 'wd').send_keys('python3')

# 通过文本链接来定位
# web.find_element(By.LINK_TEXT, 'hao123').click()
# 通过文本链接定位(包含元素就可以定位)
# web.find_element(By.PARTIAL_LINK_TEXT, 'hao').click()

# 通过元素名称来定位
href = web.find_element(By.TAG_NAME, 'a').get_attribute('href')
print(href)

time.sleep(1)
web.quit()
