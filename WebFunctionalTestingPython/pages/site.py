from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

BASE_URL = "https://the-internet.herokuapp.com"

class Site:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 12)

    def open(self, path):
        self.driver.get(BASE_URL + path)

    def visible(self, by, value):
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def clickable(self, by, value):
        return self.wait.until(EC.element_to_be_clickable((by, value)))

    def login(self, username, password):
        self.open('/login')
        self.visible(By.ID, 'username').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.clickable(By.CSS_SELECTOR, 'button[type="submit"]').click()
        return self.visible(By.ID, 'flash').text

    def checkboxes(self):
        self.open('/checkboxes')
        boxes = self.driver.find_elements(By.CSS_SELECTOR, '#checkboxes input[type="checkbox"]')
        if not boxes[0].is_selected():
            boxes[0].click()
        if boxes[1].is_selected():
            boxes[1].click()
        return [box.is_selected() for box in boxes]

    def dropdown(self):
        self.open('/dropdown')
        select = Select(self.visible(By.ID, 'dropdown'))
        select.select_by_visible_text('Option 2')
        return select.first_selected_option.text

    def javascript_alert(self):
        self.open('/javascript_alerts')
        self.clickable(By.XPATH, "//button[text()='Click for JS Confirm']").click()
        alert = self.wait.until(EC.alert_is_present())
        message = alert.text
        alert.dismiss()
        return message, self.visible(By.ID, 'result').text

    def new_window(self):
        self.open('/windows')
        original = self.driver.current_window_handle
        self.clickable(By.LINK_TEXT, 'Click Here').click()
        self.wait.until(EC.number_of_windows_to_be(2))
        other = next(h for h in self.driver.window_handles if h != original)
        self.driver.switch_to.window(other)
        heading = self.visible(By.TAG_NAME, 'h3').text
        self.driver.close()
        self.driver.switch_to.window(original)
        return heading, self.driver.current_window_handle == original

    def iframe_text(self):
        self.driver.get("https://the-internet.herokuapp.com/iframe")
        wait = WebDriverWait(self.driver, 15)

        # Wait for the iframe and switch into it
        wait.until(
        EC.frame_to_be_available_and_switch_to_it(
            (By.ID, "mce_0_ifr")
        )
        )

        editor = wait.until(
        EC.visibility_of_element_located((By.ID, "tinymce"))
        )

        # Replace existing editor content
        editor.click()
        editor.send_keys(Keys.COMMAND, "a")
        editor.send_keys("Selenium iframe test")

        # Read the content directly from the editor body
        text = editor.get_attribute("textContent")

        self.driver.switch_to.default_content()
        return text
