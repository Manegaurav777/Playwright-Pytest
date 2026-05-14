import re
from playwright.sync_api import Page, expect

from pages.automation_practice_page import AutomationPracticePage
from pages.login import LoginPage


def test_login(page: Page):
    Lp=LoginPage(page)
    Lp.goto()
    Lp.EnterUsername("student")
    Lp.EnterPassword("Password123")
    Lp.ClickSUbmit()
    print("Login test completed successfully!")
    
def test_Verify_errorMessage_wrongPassword(page: Page): 
    Lp=LoginPage(page)
    Lp.goto()
    Lp.EnterUsername("student")
    Lp.EnterPassword("Password1234")
    Lp.ClickSUbmit()
    Lp.Verify_errorMessageforwrongPassword()
    print("Error message verification test completed successfully!")
    
def test_Verify_errorMessage_wrongUsername(page: Page):
    Lp=LoginPage(page)
    Lp.goto()
    Lp.EnterUsername("Student1")
    Lp.EnterPassword("Password1234")
    Lp.ClickSUbmit()
    Lp.Verify_errorMessageForWrongUsername()
    print("Error message verification for wrong username test completed successfully!")
    print("hello")