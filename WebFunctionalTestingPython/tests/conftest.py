from pathlib import Path
import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1400,900')
    browser = webdriver.Chrome(options=options)  # Selenium Manager handles ChromeDriver
    yield browser
    if request.node.rep_call_failed:
        screenshots = Path('screenshots')
        screenshots.mkdir(exist_ok=True)
        safe_name = ''.join(c if c.isalnum() or c in '-_' else '_' for c in request.node.name)
        browser.save_screenshot(str(screenshots / f'{safe_name}.png'))
    browser.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call':
        item.rep_call_failed = report.failed
