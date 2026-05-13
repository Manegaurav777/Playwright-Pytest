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