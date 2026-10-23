from pages.site import Site

def test_checkboxes_and_dropdown(driver):
    site = Site(driver)
    assert site.checkboxes() == [True, False]
    assert site.dropdown() == 'Option 2'

def test_javascript_confirm(driver):
    message, result = Site(driver).javascript_alert()
    assert message == 'I am a JS Confirm'
    assert result == 'You clicked: Cancel'
