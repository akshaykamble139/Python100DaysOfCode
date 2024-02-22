import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

URL = ("https://www.linkedin.com/jobs/search/?currentJobId=3803659838"
       "&f_AL=true&f_WT=2&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)

driver.get(URL)

sign_in_button = driver.find_element(By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
sign_in_button.click()

email_input = driver.find_element(By.ID, value="username")
email_input.send_keys(EMAIL)
password = driver.find_element(By.ID, value="password")
password.send_keys(PASSWORD)

submit_button = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
submit_button.click()

time.sleep(4)
jobs = driver.find_elements(By.CSS_SELECTOR, value='.scaffold-layout__list-container li div div div div div a strong')
for a in jobs:
    a.click()
    save_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button/span[1]')
    save_button.click()
    # print(a.text)

# driver.quit()
