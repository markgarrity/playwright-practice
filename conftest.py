import pytest
from playwright.sync_api import Page

# Authenticated page fixture — reuse across test files
# so you don't repeat login steps everywhere
@pytest.fixture
def authenticated_page(page: Page):
    page.goto("/app/login.html")
    page.get_by_label("Email").fill("user@example.com")
    page.get_by_label("Password").fill("password123")
    page.get_by_role("button", name="Sign in").click()
    page.wait_for_url("**/app/index.html")
    return page