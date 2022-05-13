from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    web = p.chromium.launch(headless=False)
    context = web.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com/")
    page.locator('//*[@id="kw"]').fill('周杰伦')
    page.click('text=百度一下')
    print(page.title())
    page.wait_for_timeout(2000)
    page1 = context.new_page()
    context.close()
    web.close()

# from playwright.sync_api import Playwright, sync_playwright, expect
#
#
# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#
#     # Open new page
#     page = context.new_page()
#
#     # Go to https://www.baidu.com/
#     page.goto("https://www.baidu.com/")
#
#     # ---------------------
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     run(playwright)
