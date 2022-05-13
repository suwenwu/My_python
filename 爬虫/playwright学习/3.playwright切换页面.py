from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, channel='chrome')
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://zj.58.com/
    page.goto("https://zj.58.com/")

    # click 全职按钮
    # page.click('//*[@id="zpNav"]/em/a[1]')
    # page.wait_for_timeout(2000)
    # print(page.title(), page.url)

    # 检查是否切换页面
    with context.expect_page() as new_page_info:
        page.click('//*[@id="zpNav"]/em/a[1]')
    new_page = new_page_info.value

    new_page.wait_for_load_state()
    print(new_page.title())

    page.close()
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
