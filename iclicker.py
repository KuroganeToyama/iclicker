from selenium import webdriver
from selenium.webdriver.common.by import By
from delays import wait_click, wait_page
from login import login
import time
import os, shutil, sys

## Important constants
from config import EMAIL, PASSWORD, DOWNLOAD_PATH, EXCEPTIONS
ICLICKER_CLOUD_LOGIN_URL = 'https://instructor.iclicker.com/#/onboard/login'

## Helper functions

def create_folder(path):
    """Create a folder if it doesn't exist."""
    try:
        os.mkdir(path)
    except FileExistsError:
        print(f'ERROR: Folder "{path}" already exists.')
        sys.exit()

def move_files(src_path, dest_path, prefix):
    """Move files with a specific prefix to a destination folder."""
    files = os.listdir(src_path)
    files_to_move = [file for file in files if file.startswith(prefix)]
    for file in files_to_move:
        src_file = os.path.join(src_path, file)
        dest_file = os.path.join(dest_path, file)
        if os.path.isfile(src_file):
            shutil.move(src_file, dest_file)

def export_activity(driver, button_xpath, modal_button_xpath):
    """Export activity by clicking buttons."""
    wait_click(driver, 'xpath', button_xpath)
    time.sleep(2)
    wait_click(driver, 'xpath', modal_button_xpath)
    time.sleep(2)
    wait_click(driver, 'xpath', modal_button_xpath.replace('[2]', ''))

def handle_poll(driver, poll_button, section_name):
    """Handle exporting polls."""
    poll_button_text = poll_button.text.strip()
    if "Poll" in poll_button_text and poll_button_text not in EXCEPTIONS[section_name]:
        poll_button.click()
        wait_page(driver)
        export_activity(driver, 
                        '/html/body/app-root/div/app-admin/div/div/app-course/main/app-class-history/app-activity/div/div/div[1]/div[1]/button',
                        '/html/body/app-root/div/app-modals-injection/app-activity-export-modal/sui-modal/div/div/div/div/form/div[3]/button[2]')
        driver.back()
        time.sleep(3)

## Main code

# Open up Google Chrome
driver = webdriver.Chrome()

# Access iClicker Cloud login page
driver.get(ICLICKER_CLOUD_LOGIN_URL)
wait_page(driver)

# Login to iClicker Cloud
login(driver, EMAIL, PASSWORD)
time.sleep(3)
try:
    error_msg = driver.find_element(By.CLASS_NAME, 'error-msg')
    print('ERROR: Your credentials were incorrect. Please try again.')
    driver.quit()
    os._exit(-1)
except:
    pass

# Collect data
section_table_locator = (By.XPATH, '/html/body/app-root/div/app-admin/div/div/app-course-list/div/main/div/div[2]/div/div[3]/div/table/tbody')
while True:
    # Grab table of sections
    section_table = driver.find_element(*section_table_locator)
    section_rows = section_table.find_elements(By.TAG_NAME, 'tr')

    # Go through each section
    for i in range(len(section_rows)):
        section_table = driver.find_element(*section_table_locator)
        section_rows = section_table.find_elements(By.TAG_NAME, 'tr')

        section_button = section_rows[i].find_element(By.TAG_NAME, 'button')
        section_button_text = section_button.text.strip()
        section_folder_path = f"{DOWNLOAD_PATH}/{section_button_text}"

        create_folder(section_folder_path)
        section_button.click()
        wait_page(driver)

        # Export all activities
        export_activity(driver, 
                        '/html/body/app-root/div/app-admin/div/div/app-course/main/app-class-history/app-activity-list/div/div[1]/div[2]/button[2]',
                        '/html/body/app-root/div/app-modals-injection/app-activity-history-export-modal/sui-modal/div/div/div/div/form/div[3]/button[2]')

        # Export polls
        poll_table_locator = (By.XPATH, '/html/body/app-root/div/app-admin/div/div/app-course/main/app-class-history/app-activity-list/div/div[2]/div/app-list/div/table/tbody')
        while True:
            # Grab table of polls
            poll_table = driver.find_element(*poll_table_locator)
            poll_rows = poll_table.find_elements(By.CLASS_NAME, 'secondaryRow')

            # Go through each poll
            for j in range(len(poll_rows)):
                poll_table = driver.find_element(*poll_table_locator)
                poll_rows = poll_table.find_elements(By.CLASS_NAME, 'secondaryRow')

                poll_button = poll_rows[j].find_element(By.TAG_NAME, 'button')
                handle_poll(driver, poll_button, section_button_text)
            
            break

        # Move all downloaded files to corresponding section folder
        move_files(DOWNLOAD_PATH, section_folder_path, 'iClicker_')

        # Go back to table of sections
        driver.back()
        time.sleep(3)

    break
        
driver.quit()
print('Program executed successfully!')