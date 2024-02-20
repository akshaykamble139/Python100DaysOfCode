from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)

# driver.get(url="https://en.wikipedia.org/wiki/Main_Page")
#
# count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
#
# # count.click()
#
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# # all_portals.click()
#
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# driver.get("https://secure-retreat-92358.herokuapp.com/")
# first_name = driver.find_element(By.NAME, value="fName")
# last_name = driver.find_element(By.NAME, value="lName")
# email = driver.find_element(By.NAME, value="email")
#
# first_name.send_keys("Akshay")
# first_name.send_keys(Keys.ENTER)
#
# last_name.send_keys("Kamble")
# last_name.send_keys(Keys.ENTER)
#
# email.send_keys("akshay@gmail.com")
# email.send_keys(Keys.ENTER)
#
# button = driver.find_element(By.CSS_SELECTOR, value=".btn btn-lg btn-primary btn-block")
# button.click()


driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
ids = [a.get_attribute("id") for a in items]

start = time.time()
timeout = start + 5
while True:
    now = time.time()
    cookie.click()
    if now-start >= 300:
        break
    if now>timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        prices = []
        for a in all_prices:
            if a.text != "":
                prices.append(int(a.text.split("-")[1].strip().replace(",","")))

        current_cookie_elem = driver.find_element(By.ID, "money").text
        current_count = int(current_cookie_elem.replace(",", ""))

        max_index = -1
        for i in range(len(prices)):
            if current_count >= prices[i]:
                max_index = i
            else:
                break

        buy_upgrade_id = ids[max_index]
        upgrade = driver.find_element(By.ID, buy_upgrade_id)
        upgrade.click()

        timeout = time.time() + 5

    cookie.click()

# driver.quit()
