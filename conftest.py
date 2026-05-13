import sys
import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright

# Add project root to sys.path for imports
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))


@pytest.fixture
def browser_page(url="https://testautomationpractice.blogspot.com/p/playwrightpractice.html"):
    """Fixture that opens Chrome browser, navigates to URL, and closes after test"""
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    # Navigate to the URL
    page.goto(url)
    
    yield page
    
    # Cleanup after test completes
    context.close()
    browser.close()
    playwright.stop()