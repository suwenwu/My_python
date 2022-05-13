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

    # 进入登陆页面之后，添加新地址
    page.click('text=地址管理')
    page.click('text=增加新地址')

    page.fill('//*[@id="address_form"]/div[2]/div/div[2]/div[1]/div/input', '张三')
    page.fill('//*[@id="address_form"]/div[2]/div/div[2]/div[2]/div/input', '15213420987')
    page.locator('//*[@id="province"]').select_option(index=1)
    page.wait_for_timeout(1000)
    page.locator('//*[@id="city"]').select_option(index=1)
    page.wait_for_timeout(1000)
    page.locator('//*[@id="district"]').select_option(index=1)
    page.wait_for_timeout(1000)
    page.locator('//*[@id="twon"]').select_option(index=1)
    page.fill('//*[@id="address_form"]/div[2]/div/div[2]/div[4]/div/input', '天庭')
    page.click('//*[@id="address_submit"]')

    # 获取选择器的所有选项
    # nodes = page.query_selector_all('//*[@id="province"]')
    # for node in nodes:
    #     print(node.text_content())
    page.wait_for_timeout(3000)

    # 删除地址
    # page.click('//ul[@class="add_conta"]/li[4]/a[2]')

    # 等待五秒
    page.wait_for_timeout(5000)
    page.close()
    # ---------------------
    context.close()
    browser.close()


if __name__ == '__main__':
    with sync_playwright() as playwright:
        run(playwright)
