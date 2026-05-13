from playwright.sync_api import expect
from .base_page import BasePage


class AutomationPracticePage(BasePage):
    URL = "https://testautomationpractice.blogspot.com/p/playwrightpractice.html"

    def goto(self) -> None:
        super().goto(self.URL)

    @property
    def heading(self):
        return self.page.get_by_text("Automation Testing Practice")

    @property
    def buttons_heading(self):
        return self.page.get_by_role("heading", name="Buttons")

    @property
    def description_text(self):
        return self.page.get_by_text("Locate elements by their text content.")

    @property
    def username_input(self):
        return self.page.get_by_label("Username:")

    @property
    def email_input(self):
        return self.page.get_by_label("Email Address:")

    @property
    def password_input(self):
        return self.page.get_by_label("Password:")

    @property
    def submit_form_button(self):
        return self.page.get_by_role("button", name="Submit Form")

    @property
    def accept_terms_checkbox(self):
        return self.page.get_by_role("checkbox", name="Accept terms")

    @property
    def start_button(self):
        return self.page.get_by_role("button", name="START")

    @property
    def full_name_input(self):
        return self.page.get_by_placeholder("Enter your full name")

    @property
    def phone_input(self):
        return self.page.get_by_placeholder("Phone number (xxx-xxx-xxxx)")

    @property
    def message_input(self):
        return self.page.get_by_placeholder("Type your message here...")

    @property
    def product_search_input(self):
        return self.page.get_by_placeholder("Search products...")

    @property
    def search_button(self):
        return self.page.get_by_role("button", name="Search")

    @property
    def logo_image(self):
        return self.page.get_by_alt_text("logo image")

    @property
    def home_link(self):
        return self.page.get_by_title("Home page link")

    @property
    def profile_name(self):
        return self.page.get_by_test_id("profile-name")

    @property
    def upload_files_title(self):
        return self.page.get_by_title("Upload Files")

    @property
    def combo_box(self):
        return self.page.locator("//input[@id='comboBox']")

    @property
    def dropdown_option(self):
        return self.page.locator("//div[@id='dropdown']//div[@class='option' and text()='Item 3']")

    @property
    def draggable(self):
        return self.page.locator("//div[@id='draggable']")

    @property
    def droppable(self):
        return self.page.locator("//div[@id='droppable']")

    def fill_username(self, username: str) -> None:
        self.username_input.fill(username)

    def fill_email(self, email: str) -> None:
        self.email_input.fill(email)

    def fill_password(self, password: str) -> None:
        self.password_input.fill(password)

    def click_submit_form(self) -> None:
        self.submit_form_button.click()

    def accept_terms(self) -> None:
        self.accept_terms_checkbox.click()

    def click_start(self) -> None:
        self.start_button.click()

    def fill_start_form(self, full_name: str, phone: str, message: str) -> None:
        self.full_name_input.fill(full_name)
        self.phone_input.fill(phone)
        self.message_input.fill(message)

    def search_product(self, product_name: str) -> None:
        self.product_search_input.fill(product_name)
        self.search_button.click()

    def select_dropdown_item(self) -> None:
        self.combo_box.click()
        self.dropdown_option.click()

    def drag_item_to_drop(self) -> None:
        self.draggable.drag_to(self.droppable)
    
    def  get_byROle(self) -> None:
        return self.page.get_by_role("alert", name="This is an important alert message!")   
