from playwright.sync_api import Page, expect

def test_successful_login_redirects_to_dashboard(page: Page):
    page.goto("/app/login.html")
    page.get_by_label("Email").fill("user@example.com")
    page.get_by_label("Password").fill("password123")
    page.get_by_role("button", name="Sign in").click()

    expect(page.get_by_role("heading", name="Welcome to the Dashboard")).to_be_visible()

def test_invalid_credentials_shows_error(page: Page):
    page.goto("/app/login.html")
    page.get_by_label("Email").fill("wrong@example.com")
    page.get_by_label("Password").fill("badpass")
    page.get_by_role("button", name="Sign in").click()

    expect(page.get_by_text("Invalid email or password")).to_be_visible()

def test_error_not_visible_on_page_load(page: Page):
    page.goto("/app/login.html")
    expect(page.locator("#error")).to_be_hidden()