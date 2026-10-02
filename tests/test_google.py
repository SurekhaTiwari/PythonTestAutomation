import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = Options()
    #options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    d = webdriver.Chrome(options=options)
    yield d
    d.quit()


def test_google_title(driver):
    driver.get("https://www.google.com")
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "q")))
    assert "Google" in driver.title