from config import *
from bash import *
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime, timedelta
import os

def execute_login():
    try:
        email_form = driver.find_element_by_name("email")
        password_form = driver.find_element_by_name("password")
        email_form.send_keys(DEMO_EMAIL)
        password_form.send_keys(DEMO_PASSWORD)
        driver.find_element_by_css_selector(".btn.button-orange").click()
    except:
        print("Already logged in...")

def enter_end_point(ep):
    try:
        tab_selector = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, ep)))
        driver.execute_script("arguments[0].click();", tab_selector)
    except TimeoutException:
        print("Unable to locate element, exiting...")

def execute_end_point(ep):
    try:
        if ep != "tab-slowrequest":
            execute_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "execute")))
            execute_button.click()
        else:
            for ap in api_list:
                try:
                    dropdown_selector = Select(WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "apicall"))))
                    dropdown_selector.select_by_visible_text(ap)
                    execute_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "execute")))
                    execute_button.click()
                except Exception:
                    driver.refresh()
                    print("Unable to locate element in dropdown exiting...")
    except TimeoutException:
        driver.refresh()
        print("Unable to locate element, exiting...")

def start_deploy(apptype):
    if apptype == "good":
        os.system(start_good_deployment)
    else:
        os.system(start_bad_deployment)
def complete_deploy(apptype):
    if apptype == "good":
        os.system(complete_good_deployment)
    else:
        os.system(complete_bad_deployment)


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=chrome_options)


while True:
    start_time = datetime.now()
    first_four_hours = start_time + timedelta(hours=4)
    last_four_hours = first_four_hours + timedelta(hours=4)
    first_count = 0
    start_deploy("good")
    complete_deploy("good")
    while (datetime.now() < first_four_hours):
        try:
            driver.get(GOOD_APP)
        except Exception:
            print("Unable to load page, refreshing...")
            driver.refresh()
        execute_login()
        for ep in end_points:
            enter_end_point(ep)
            execute_end_point(ep)
            time.sleep(2)
        first_count += 1
        print("Complete Sequence, Good App {}".format(first_count))
    second_count = 0
    start_deploy("bad")
    complete_deploy("bad")
    while (datetime.now() < last_four_hours):
        try:
            driver.get(BAD_APP)
        except Exception:
            print("Unable to load page, refreshing...")
            driver.refresh()
        execute_login()
        for ep in end_points:
            enter_end_point(ep)
            execute_end_point(ep)
            time.sleep(2)
        second_count += 1
        print("Complete Sequence, Bad App {}".format(second_count))
