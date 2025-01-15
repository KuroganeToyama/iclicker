from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Literal
import time

# Patient click, works for 'id', 'name', 'xpath', 'class'
def wait_click(driver: WebDriver, type: Literal['id', 'name', 'xpath', 'class'], name, retries=3, delay=2):
    for _ in range(retries):
        if type == 'class':
            type = By.CLASS_NAME
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((type, name)))
            element.click()
            return  # If successful, exit function
        except (Exception) as e:
            print(f"Exception caught: {e}. Retrying...")
            time.sleep(delay)
    print("Couldn't detect presence of element or element is not clickable.")

# Wait for page to fully load before interacting
def wait_page(driver: WebDriver, timeout=15):
    def page_loaded(driver: WebDriver):
        return driver.execute_script("return document.readyState") == "complete"
    WebDriverWait(driver, timeout).until(page_loaded)