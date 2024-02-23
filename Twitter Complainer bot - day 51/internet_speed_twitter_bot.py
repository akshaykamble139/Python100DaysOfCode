from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

TWITTER_LOGIN_URL = 'https://twitter.com/i/flow/login'
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

PROMISED_SPEED = 250.0
PROMISED_UP = 200.0
INTERNET_SPEED_WEBSITE = "https://www.speedtest.net/"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.chrome_options)
        self.down = 0.0
        self.up = 0.0

    def get_internet_speed(self):
        self.driver.get(INTERNET_SPEED_WEBSITE)
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        cookie_button = self.driver.find_element(By.ID, 'onetrust-accept-btn-handler')
        time.sleep(50)
        cookie_button.click()

        congrats_popup_ok_button = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button'
        )
        congrats_popup_ok_button.click()

        time.sleep(10)

        speeds = self.driver.find_elements(
            By.CLASS_NAME, 'result-data-large')

        i = 0

        arr = []
        for speed in speeds:
            arr.append(speed.text)

        print(arr)
        # ['222.07', '160.39']

        self.down = arr[0]
        self.up = arr[1]
        self.driver.quit()

    def tweet_at_provider(self):
        self.driver.get(TWITTER_LOGIN_URL)
        self.driver.maximize_window()
        time.sleep(3)
        email_input = self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]'
                      '/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
        )
        email_input.send_keys(TWITTER_EMAIL)
        email_input.send_keys(Keys.ENTER)

        # time.sleep(2)
        for i in range(5):
            print(i)
            time.sleep(1)

        password_input = self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]'
                      '/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]'
        )
        password_input.send_keys(TWITTER_PASSWORD)
        time.sleep(1)
        password_input.send_keys(Keys.ENTER)

        post_a_tweet = self.driver.find_element(
            By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div'
        )
        post_a_tweet.click()

        tweet_input = self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]'
                      '/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div['
                      '2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div['
                      '2]/div/div/div/div'
        )

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_SPEED}down/{PROMISED_UP}up?"

        tweet_input.send_keys(tweet)

        post_button = self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/'
                      'div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/span/span'
        )

        post_button.click()