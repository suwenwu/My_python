from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, channel='chrome')
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://testingedu.com.cn:8000/Home/user/login.html
    page.goto("http://testingedu.com.cn:8000/Home/user/login.html")

    # 登陆
    page.fill('//*[@id="username"]', '13800138006')
    page.fill('//*[@id="password"]', '123456')
    page.fill('//*[@id="verify_code"]', '1111')
    page.click('//a[@class="J-login-submit"]')

    page.wait_for_timeout(1000)
    print(page.url)

    # 等待五秒
    page.wait_for_timeout(5000)
    page.close()
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
