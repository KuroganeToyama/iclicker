from selenium import webdriver
from selenium.webdriver.common.by import By
from delays import wait_click, wait_page
from login import login
import time
import os, shutil, sys

## Important constants
from config import EMAIL, PASSWORD, DOWNLOAD_PATH, EXCEPTIONS
ICLICKER_CLOUD_LOGIN_URL = 'https://instructor.iclicker.com/#/onboard/login'

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

        try:
            os.mkdir(section_folder_path)
        except:
            print(f'ERROR: Folder "{section_button_text}" already exists in {DOWNLOAD_PATH}')
            sys.exit()

        section_button.click()
        wait_page(driver)

        # Export all activites
        wait_click(driver, 'xpath', '/html/body/app-root/div/app-admin/div/div/app-course/main/app-class-history/app-activity-list/div/div[1]/div[2]/button[2]')
        time.sleep(2)

        wait_click(driver, 'xpath', '/html/body/app-root/div/app-modals-injection/app-activity-history-export-modal/sui-modal/div/div/div/div/form/div[3]/button[2]')
        time.sleep(2)

        wait_click(driver, 'xpath', '/html/body/app-root/div/app-modals-injection/app-activity-history-export-modal/sui-modal/div/div/div/div/form/div[3]/button')
        time.sleep(2)

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
                poll_button_text = poll_button.text.strip()

                if "Poll" in poll_button_text and poll_button_text not in EXCEPTIONS:
                    poll_button.click()
                    wait_page(driver)

                    wait_click(driver, 'xpath', '/html/body/app-root/div/app-admin/div/div/app-course/main/app-class-history/app-activity/div/div/div[1]/div[1]/button')
                    wait_page(driver)

                    wait_click(driver, 'xpath', '/html/body/app-root/div/app-admin/div/div/app-course/main/app-class-history/app-activity/div/div/div[1]/div[2]/li[1]/button')
                    time.sleep(2)

                    wait_click(driver, 'xpath', '/html/body/app-root/div/app-modals-injection/app-activity-export-modal/sui-modal/div/div/div/div/form/div[3]/button[2]')
                    time.sleep(2)

                    wait_click(driver, 'xpath', '/html/body/app-root/div/app-modals-injection/app-activity-export-modal/sui-modal/div/div/div/div/form/div[3]/button')
                    wait_page(driver)

                    # Go back to table of polls
                    driver.back()
                    time.sleep(3)
            
            break

        # Move all downloaded files to corresponding section folder
        files = os.listdir(DOWNLOAD_PATH)
        files_to_move = [file for file in files if file.startswith('iClicker_')]
        for file in files_to_move:
            src_file = os.path.join(DOWNLOAD_PATH, file)
            dest_file = os.path.join(section_folder_path, file)
            if os.path.isfile(src_file):
                shutil.move(src_file, dest_file)

        # Go back to table of sections
        driver.back()
        time.sleep(3)

    break
        
driver.quit()
print('Program executed successfully!')