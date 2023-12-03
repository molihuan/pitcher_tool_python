from playwright.sync_api import sync_playwright


def run(playwright):
    # 这里填入步骤 2 中获取到的 WebSocket URL
    ws_endpoint = "ws://127.0.0.1:9222/devtools/browser/5e50cd10-13cb-41e5-88d3-552c5a1e517e"

    browser = playwright.chromium.connect_over_cdp(endpoint_url=ws_endpoint)

    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com/")
    print(page.title())
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
