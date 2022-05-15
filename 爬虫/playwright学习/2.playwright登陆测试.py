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
    page.wait_for_selector('//*[@id="province"]').select_option(label='山东省')
    page.wait_for_selector('//*[@id="city"]').select_option(index=2)
    page.wait_for_selector('//*[@id="district"]').select_option(index=2)
    try:
        page.wait_for_selector('//*[@id="twon"]', timeout=1000).select_option(index=2)
    except:
        print('没有选择区')
    page.fill('//*[@id="address_form"]/div[2]/div/div[2]/div[4]/div/input', '天庭')
    page.click('//*[@id="address_submit"]')

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
