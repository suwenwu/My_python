from selenium import webdriver

web = webdriver.Chrome()

web.get('https://www.baidu.com')

print(web.title)

# web.quit()
