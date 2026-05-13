import re
from playwright.sync_api import Page, expect

from pages.automation_practice_page import AutomationPracticePage


def test_get_started_link(page: Page):
    automation_page = AutomationPracticePage(page)
    automation_page.goto()

    expect(automation_page.heading).to_be_visible()
    automation_page.fill_username("xyz@gmail.com")

    expect(automation_page.buttons_heading).to_be_visible()
    expect(automation_page.description_text).to_contain_text("by")

    automation_page.click_submit_form()
    automation_page.fill_email("xyz@gmail.com")
    automation_page.fill_password("12345678")

    expect(page).to_have_title(re.compile("Automation Testing Practice: PlaywrightPractice"))

    automation_page.accept_terms()
    expect(automation_page.accept_terms_checkbox).to_be_checked()

    automation_page.click_start()
    automation_page.fill_start_form("John Doe", "123-456-7890", "This is a test message.")
    automation_page.search_product("Laptop")

    expect(automation_page.logo_image).to_be_visible()
    expect(automation_page.home_link).to_be_visible()
    expect(automation_page.profile_name).to_be_visible()
    #expect(automation_page.upload_files_title).to_be_visible()

    automation_page.select_dropdown_item()
    automation_page.drag_item_to_drop()

    automation_page.wait_for_timeout(5000)
    print("Test completed successfully!")
    print("All assertions passed without exceptions.")
    print("Test execution finished.")
    print("Check video is working fine or not")
    print("Its Raining in my city")