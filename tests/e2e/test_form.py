from playwright.sync_api import Page, expect

def test_email_field_accepts_input(page: Page):
    page.goto("/app/login.html")
    page.get_by_label("Email").fill("test@example.com")
    expect(page.get_by_label("Email")).to_have_value("test@example.com")

def test_password_field_masks_input(page: Page):
    page.goto("/app/login.html")
    password_input = page.get_by_label("Password")
    expect(password_input).to_have_attribute("type", "password")

def test_error_clears_on_valid_login_after_failure(page: Page):
    # First fail
    page.goto("/app/login.html")
    page.get_by_label("Email").fill("wrong@example.com")
    page.get_by_label("Password").fill("badpass")
    page.get_by_role("button", name="Sign in").click()
    expect(page.get_by_text("Invalid email or password")).to_be_visible()

    # Then succeed
    page.get_by_label("Email").fill("user@example.com")
    page.get_by_label("Password").fill("password123")
    page.get_by_role("button", name="Sign in").click()
    expect(page.get_by_role("heading", name="Welcome to the Dashboard")).to_be_visible()