from typing import Literal
from selenium.webdriver.remote.webdriver import WebDriver

# Performs field entry
# This function locates an input field using the specified type and name, clears its content, and enters new content.
def field_entry(driver: WebDriver, type: Literal['id', 'name'], name: str, content: str):
    input = driver.find_element(type, name)  
    input.clear()
    input.send_keys(content)