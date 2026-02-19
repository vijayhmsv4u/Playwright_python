from playwright.sync_api import Page

class loginPage:
    def __init__(self,page:Page):
        self.page=page
        self.username=page.get_by_role("textbox", name="Username")
        self.password=page.get_by_role("textbox", name="Password")
        self.login_btn=page.get_by_role("button", name="Login")

    def enter_username(self,username:str):
        self.username.fill("Admin")

    def enter_password(self,password:str):
        self.password.fill("admin123")
    def click_login(self):
        self.login_btn.click()

    def login(self,username:str,password:str):
        self.username.fill("Admin")
        self.password.fill("admin123")
        self.login_btn.click()


    
