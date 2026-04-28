from playwright.sync_api import Page, expect

def test_login_page_has_required_fields(page: Page):
    page.goto("/app/login.html")
    expect(page.get_by_label("Email")).to_be_visible()
    expect(page.get_by_label("Password")).to_be_visible()
    expect(page.get_by_role("button", name="Sign in")).to_be_visible()

def test_dashboard_has_nav_links(authenticated_page):
    expect(authenticated_page.get_by_role("link", name="Login")).to_be_visible()
    expect(authenticated_page.get_by_role("link", name="About")).to_be_visible()

def test_dashboard_shows_logged_in_message(authenticated_page):
    expect(authenticated_page.get_by_text("You are logged in.")).to_be_visible()