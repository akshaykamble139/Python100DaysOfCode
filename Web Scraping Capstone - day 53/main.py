from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time

ZILLOW_CLONE_URL = 'https://appbrewery.github.io/Zillow-Clone/'

GOOGLE_RESEARCH_FORM = ('https://docs.google.com/forms/d/e/'
                        '1FAIpQLSde3h8XztF1y9nYswfuPQPhB6da5rsNFaz7fFdFeugXsWfv4A/viewform?usp=sf_link')

response = requests.get(url=ZILLOW_CLONE_URL)
response.raise_for_status()

html = response.text

soup = BeautifulSoup(html, "html.parser")
property_links = soup.select('.StyledPropertyCardPhotoBody a')
links = []
for a in property_links:
    links.append(a.get("href"))

# print(links)

property_prices = soup.select('.PropertyCardWrapper__StyledPriceLine')
prices = []
for a in property_prices:
    price = a.text.split("/")[0]
    price = price.split("+")[0]
    prices.append(price)

# print(prices)
property_addresses = soup.select('.StyledPropertyCardDataArea-anchor address')
addresses = []
for a in property_addresses:
    address = a.text.replace('\n',"").strip()
    addresses.append(address)

# print(addresses)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)

for i in range(len(prices)):
    driver.get(url=GOOGLE_RESEARCH_FORM)
    time.sleep(1)
    link = links[i]
    price = prices[i]
    address = addresses[i]

    address_input = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )
    address_input.send_keys(address)

    price_input = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )
    price_input.send_keys(price)

    link_input = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )
    link_input.send_keys(link)

    submit = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
    )

    submit.click()


