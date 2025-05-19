from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://customeow.io/en/login")
    page.get_by_text("Continue with Email").click()
    page.get_by_placeholder("Enter your email").click()
    page.get_by_placeholder("Enter your email").fill("fjc@idd.cool")
    page.get_by_placeholder("Enter your password").click()
    page.get_by_placeholder("Enter your password").fill("Aa123456!")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Feature Sets").click()
    page.get_by_role("link", name="Design Templates").click()
    page.get_by_role("link", name="Orders").click()
    page.get_by_role("link", name="Builder Request").click()
    page.get_by_role("link", name="My Request").click()
    page.get_by_role("link", name="New Request").click()
    page.get_by_role("link", name="My Stores").click()
    page.locator("header").get_by_role("img").nth(4).click()
    page.get_by_role("menuitem", name="Invoice").click()
    page.get_by_text("Invoice").nth(1).click()
    page.locator("header").get_by_role("img").nth(4).click()
    page.get_by_role("menuitem", name="Setting").click()
    page.get_by_role("heading", name="Setting").click()
    page.locator("header").get_by_role("img").nth(4).click()
    page.get_by_role("menuitem", name="Credit Usage").click()
    page.get_by_role("button", name="Export").click()
    page.get_by_placeholder("Start date").click()
    page.locator(".mm-picker-header-label > .customeow-icon").first.click()
    page.get_by_text("2024").click()
    page.get_by_text("Jan").click()
    page.get_by_text("1", exact=True).nth(1).click()
    page.get_by_text("1", exact=True).nth(3).click()
    with page.expect_download() as download_info:
        page.get_by_role("button", name="Export CSV").click()
    download = download_info.value
    page.get_by_role("link", name="Feature Sets").click()
    page.locator("div").filter(has_text=re.compile(r"^189 ItemsActionIntegrate into stores$")).locator("span div").click()
    page.locator("div").filter(has_text=re.compile(r"^40 ItemsDeleteActionIntegrate into stores$")).locator("svg").click()
    page.locator("div:nth-child(3) > svg > path").first.click()
    page.get_by_text("Remove from favorites").click()
    page.locator("svg:nth-child(4)").first.click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
