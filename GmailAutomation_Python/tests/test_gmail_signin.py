from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_gmail_signin_email_field_is_visible(driver):
    wait = WebDriverWait(driver, 20)

    # Step 1: Open the Gmail landing page.
    driver.get("https://workspace.google.com/intl/en-US/gmail/")

    # Step 2: Find and click the Sign in link.
    sign_in = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[aria-label='Sign into Gmail']"))
    )

    original_window = driver.current_window_handle
    sign_in.click()

    # Step 3: Wait for the new tab and switch to it.
    wait.until(EC.number_of_windows_to_be(2))
    new_window = next(
        handle for handle in driver.window_handles if handle != original_window
    )
    driver.switch_to.window(new_window)

    # Step 4: Wait for the Email or phone field to become visible.
    email_field = wait.until(
        EC.visibility_of_element_located((By.ID, "identifierId"))
    )

    # Step 5: Assert that the field is displayed.
    assert email_field.is_displayed(), "Email or phone field is not visible."

    print("PASS: Email or phone field is visible.")
