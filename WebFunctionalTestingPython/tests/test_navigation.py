from pages.site import Site

def test_multiple_windows(driver):
    heading, returned_to_original = Site(driver).new_window()
    assert heading == 'New Window'
    assert returned_to_original

def test_iframe(driver):
    text = Site(driver).iframe_text()
    assert "Selenium iframe test" in text
