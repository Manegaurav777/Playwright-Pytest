from playwright.sync_api import Page
from .base_page import BasePage

class LoginPage(BasePage):
    URL="https://practicetestautomation.com/practice-test-login/"

    def goto(self) -> None:
        super().goto(self.URL)

    def EnterUsername(self,username:str) -> None:
        self.page.get_by_label("Username").fill(username)
    
    def EnterPassword(self,passwords:str) ->None:
        self.page.get_by_label("Password").fill(passwords)    
    
    def ClickSUbmit(self) -> None:
        self.page.get_by_role("button", name="Submit").click()