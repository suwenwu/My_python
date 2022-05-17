from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

options = Options()
# 开启无头模式
options.add_argument('--headless')
options.add_argument('--disable-gpu')
# 代理ip
options.add_argument('--proxy-server=http://120.42.46.226:6666')
# 跳过私密链接
options.add_argument('ignore-certificate-errors')
# 请求头
options.add_argument(
    '--user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3880.400 QQBrowser/10.8.4554.400')

web = Chrome(options=options)

web.implicitly_wait(10)

web.get('https://ssr2.scrape.center/')

print(web.page_source)
