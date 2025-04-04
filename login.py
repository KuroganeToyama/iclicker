from delays import wait_click, wait_page
from forms import field_entry
from selenium.webdriver.remote.webdriver import WebDriver

# Function to log in to the application.
# Parameters:
# driver: WebDriver instance to interact with the browser.
# username: User's email address.
# password: User's password.
def login(driver: WebDriver, username: str, password: str):
    field_entry(driver, 'id', 'email', username)
    field_entry(driver, 'id', 'password', password)
    wait_click(driver, 'xpath', '/html/body/app-root/div/app-onboard/div/app-auth/app-login/app-new-login/div/div[1]/div/div[1]/form/div[5]/button[1]')
    wait_page(driver)