import re
from playwright.sync_api import Page, sync_playwright, expect
from pages.OrageHRM_Home_page import homePage
from pages.orangeHRM_login_page import loginPage

def test_example(page:Page)->None:
    
    login_page =loginPage(page)
    home_page=homePage(page)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()

    home_page.click_leave_menu()
    home_page.logout()



