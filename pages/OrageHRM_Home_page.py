from playwright.sync_api import Page,expect

class homePage:
    def __init__(self,page:Page):
        self.page=page
        self.pageheading=page.get_by_role("heading")
        self.logged_in_user =page.get_by_role("banner")
        self.profile_btn =page.get_by_role("banner").get_by_role("img", name="profile picture")
        self.logout_btn =page.get_by_role("menuitem", name="Logout")
        self.leave_menu =page.get_by_role("link", name="Leave")
        self.leave_header =page.locator("h6")
        

    def profile(self):
        expect(self.logged_in_user).to_contain_text("john_snow akhil user Dawud")
    def click_leave_menu(self):
        self.leave_menu.click()
        expect(self.leave_header).to_contain_text("Leave")

    def logout(self):
        self.profile_btn.click()
        self.logout_btn.click()
    

    