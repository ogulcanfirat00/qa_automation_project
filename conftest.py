import os
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    is_ci = os.getenv("CI") == "true"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=is_ci,   # CI → True, Local → False
            slow_mo=0 if is_ci else 300
        )
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080}
    )
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()