from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# driver.get(url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
#
# captcha = driver.find_element(By.LINK_TEXT, "Try different image")
# captcha.click()
#
# price_dollars = driver.find_element(By.CLASS_NAME, "a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction").text
#
# print(f"The price is {price_dollars}.{price_cents}")


driver.get(url="https://www.python.org/")

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))
#
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
#
# link = driver.find_element(By.CSS_SELECTOR, value= ".documentation-widget a")
# print(link.text)
#
# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

upcoming_events_dict = {}

for i in range(5):
    event_date = driver.find_element(By.XPATH,
                                      value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i+1}]/time').text
    event_name = driver.find_element(By.XPATH,
                                      value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i+1}]/a').text

    upcoming_events_dict[i] = {
        "time": event_date,
        "name": event_name
    }

print(upcoming_events_dict)
# To close one tab
# driver.close()
# To close the  window with all tabs
driver.quit()
