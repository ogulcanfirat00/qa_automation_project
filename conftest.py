import os
import pytest
import base64
from pytest_html import extras
from datetime import datetime
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
    
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)

        if page:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_path = f"reports/screenshots/{item.name}_{timestamp}.png"

            page.screenshot(path=screenshot_path, full_page=True)
            
            with open(screenshot_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

            extra = getattr(report, "extras", [])
            extra.append(extras.image(encoded_image, mime_type="image/png"))
            report.extras = extra