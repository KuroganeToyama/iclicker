from typing import Literal
from selenium.webdriver.remote.webdriver import WebDriver

# Performs field entry
def field_entry(driver: WebDriver, type: Literal['id', 'name'], name: str, content: str):
    input = driver.find_element(type, name)  
    input.clear()
    input.send_keys(content)