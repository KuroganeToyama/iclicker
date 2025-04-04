from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Literal
import time

# Patient click, works for 'id', 'name', 'xpath', 'class'
def wait_click(driver: WebDriver, type: Literal['id', 'name', 'xpath', 'class'], name: str, retries: int = 3, delay: int = 2) -> None:
    for _ in range(retries):
        if type == 'class':
            type = By.CLASS_NAME
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((type, name)))
            element.click()
            return  # If successful, exit function
        except Exception as e:
            print(f"Exception caught while trying to click element '{name}' of type '{type}': {e}. Retrying...")
            time.sleep(delay)
    print(f"Couldn't detect presence of element '{name}' or element is not clickable after {retries} retries.")

# Wait for page to fully load before interacting
def wait_page(driver: WebDriver, timeout: int = 15) -> None:
    def page_loaded(driver: WebDriver) -> bool:
        return driver.execute_script("return document.readyState") == "complete"
    WebDriverWait(driver, timeout).until(page_loaded)