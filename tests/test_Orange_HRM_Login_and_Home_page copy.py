import re
from playwright.sync_api import Page, sync_playwright, expect


def test_exmaplerun(page) -> None:

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.wait_for_timeout(5000)
    expect(page.get_by_role("heading")).to_contain_text("Dashboard")
    page.get_by_role("link", name="Leave").click()
    expect(page.locator("h6")).to_contain_text("Leave")
    page.get_by_role("link", name="Performance").click()
    expect(page.get_by_role("banner")).to_contain_text("Performance")
    page.get_by_role("banner").get_by_role("img", name="profile picture").click()
    page.get_by_role("menuitem", name="Logout").click()
    expect(page.get_by_role("heading")).to_contain_text("Login")


