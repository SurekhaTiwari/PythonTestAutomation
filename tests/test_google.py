import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--headless=new")  # optional
    d = webdriver.Chrome(options=options)
    yield d
    d.quit()

def test_google_title(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title