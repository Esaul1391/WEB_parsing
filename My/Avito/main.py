from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Переход на страницу авито
    page.goto('https://www.avito.ru/')
    search_input = page.locator('input[data-marker="search-form/suggest"]').type(text='dfsdf'.keyword, delay=0.3)
