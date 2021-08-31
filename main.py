from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from config import *
import time

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")

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
        # element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "tab-logout")))
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
                except TimeoutException:
                    driver.refresh()
                    print("Unable to locate element in dropdown exiting...")
    except TimeoutException:
        driver.refresh()
        print("Unable to locate element, exiting...")


driver.get("http://127.0.0.1:5000/")
execute_login()
for ep in end_points:
    enter_end_point(ep)
    execute_end_point(ep)
    time.sleep(2)
print("Complete Sequence")