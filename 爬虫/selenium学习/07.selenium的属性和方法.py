import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

url = 'https://spa1.scrape.center/'
web = Chrome()

web.get(url)

time.sleep(2)

# 查看网页渲染过后的源码（有时候需要等待渲染结束再查看）
# print(web.page_source)

# 显示响应对应的url
# print(web.current_url)
# 显示响应标题
# print(web.title)
while True:
    next_page = web.find_element(By.XPATH, '//button[@class="btn-next"]')
    divs = web.find_elements(By.XPATH, '//*[@id="index"]/div[1]/div[1]/div')
    for div in divs:
        move_name = div.find_element(By.XPATH, './/h2').text
        print(move_name)
    print("--------------------------------------------------------")
    if next_page.is_enabled():
        next_page.click()
        time.sleep(1)
        windows = web.window_handles
        web.switch_to.window(windows[0])
    else:
        time.sleep(1)
        break

# web.close()     #关闭当前焦点所在的窗口
# web.quit()       #关闭所有窗口，并且安全关闭sessio
web.quit()
