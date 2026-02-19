from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Set True for headless
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.wait_for_timeout(10000)
    page.title()
    print("Page title:",page.title())

    browser.close()