from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
import os

INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

SIMILAR_ACCOUNT = "https://www.instagram.com/chefsteps/"


class InstaFollower:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(3)
        username = self.driver.find_element(
            By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'
        )
        username.send_keys(INSTAGRAM_USERNAME)
        username.send_keys(Keys.ENTER)

        password = self.driver.find_element(
            By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input'
        )
        password.send_keys(INSTAGRAM_PASSWORD)
        password.send_keys(Keys.ENTER)

        login_button = self.driver.find_element(
            By.XPATH, '//*[@id="loginForm"]/div/div[3]'
        )
        login_button.click()

        time.sleep(5)

        # save_info_not_now_button = (
        # self.driver.find_element(
        #     By.XPATH, '//*[@id="mount_0_0_Fe"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div'
        # ))
        # '//*[@id="mount_0_0_RI"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div'
        save_info_not_now_button = self.driver.find_elements(
            By.CSS_SELECTOR, 'section main div div div div div'
        )

        for a in save_info_not_now_button:
            if a.text == "Not now":
                a.click()

        time.sleep(2)

        notification_off_button = self.driver.find_elements(
            By.CSS_SELECTOR, 'div div div div div div div div div div button'
        )

        for a in notification_off_button:
            if a.text == "Not Now":
                print(a.text)
                a.click()

    def find_followers(self):
        self.driver.get(SIMILAR_ACCOUNT)
        time.sleep(5)
        followers = self.driver.find_elements(
            By.CSS_SELECTOR, 'section main div header section ul li a'
        )
        for a in followers:
            t = a.text
            if t != "" and t.find("followers") != -1:
                a.click()
                time.sleep(2)
                scroll_bar = self.driver.find_element(
                    By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]'
                )
                for i in range(10):
                    bot.follow()
                    self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_bar)
                    time.sleep(2)

    def follow(self):
        follow_buttons = self.driver.find_elements(
            By.CSS_SELECTOR, 'div div div div div div div div div div div div div button'
        )
        for button in follow_buttons:
            print(button.text)
            if button.text == "Follow":
                try:
                    button.click()
                    time.sleep(1.1)
                except ElementClickInterceptedException:
                    cancel = self.driver.find_element(
                        By.XPATH, "//button[contains(text(), 'Cancel')]"
                    )
                    cancel.click()




bot = InstaFollower()

bot.login()
bot.find_followers()
