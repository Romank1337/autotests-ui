from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("user.name@gmail.com")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("username")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("password")
    page.get_by_test_id("registration-page-registration-button").click()
    DashBoardTitle = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(DashBoardTitle).to_be_visible()
