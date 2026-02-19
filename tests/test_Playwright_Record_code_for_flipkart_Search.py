import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.flipkart.com/")
    page.get_by_role("textbox", name="Search for Products, Brands").click()
    page.get_by_role("textbox", name="Search for Products, Brands").fill("mobiles")
    page.get_by_role("textbox", name="Search for Products, Brands").press("Enter")
    page.close()
    