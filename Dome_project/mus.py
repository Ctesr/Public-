from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://spotidownloader.com/")
    page.get_by_placeholder("https://open.spotify.com/.../").click()
    page.get_by_placeholder("https://open.spotify.com/.../").fill("https://open.spotify.com/track/4J1vA4sgG6FJ1j21UugbtH?si=b5a4643670914918")
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
