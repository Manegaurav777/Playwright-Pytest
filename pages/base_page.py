from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def goto(self, url: str) -> None:
        self.page.goto(url)

    def wait_for_timeout(self, ms: int) -> None:
        self.page.wait_for_timeout(ms)
