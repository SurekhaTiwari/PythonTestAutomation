import pytest
from pages.site import Site

def test_valid_login(driver):
    message = Site(driver).login('tomsmith', 'SuperSecretPassword!')
    assert 'You logged into a secure area!' in message
    assert '/secure' in driver.current_url

@pytest.mark.parametrize('username,password', [
    ('wronguser', 'SuperSecretPassword!'),
    ('tomsmith', 'wrongpassword'),
])
def test_invalid_login(driver, username, password):
    message = Site(driver).login(username, password)
    assert 'invalid!' in message
