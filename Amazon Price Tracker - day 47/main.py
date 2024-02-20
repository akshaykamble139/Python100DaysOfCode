import requests
from bs4 import BeautifulSoup
import lxml

import smtplib

AMAZON_PRODUCT_LINK = ("https://www.amazon.in/Storio-Sticker-Brainstorming-Adjustable-Tightness/dp/B085DZM4JS/ref"
                       "=sr_1_5?dib=eyJ2IjoiMSJ9"
                       ".0fqN_NytRkgzxFLBY2Pw86paU0zpn1dPF3WSAavDbogPfcPBRimImS8RYHE8e5FD2BkN_gJD5-zEZ7KzcntYkGK"
                       "-N7knqVwsMLPzMERjzkcfjRhYpwpc07PzWitZzYXdy341s6Vo0c0jQcoHnP7HgNHiTAbWXqih2OaZQbi1jzkEiV2G"
                       "pMoOtl6og9wCNJZOUSpEtzgSzELunEmnI6i31sFNI0nAV5tB7VFLLx3uUV6vMvZ_Id155VvdSC56YH59LocJpcS_Sr"
                       "TXQRADZL2MOIW1HM-WzpeDUOvEF02Eu5o.C4VBUeUJdlruW8TtRDs01ygAkmpHJvU7oVg9FM0OJbY&dib_tag=se"
                       "&keywords=Rubik%2BCube&qid=1708425369&sr=8-5&th=1")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=AMAZON_PRODUCT_LINK, headers=headers)
response.raise_for_status()

product_page_html = response.text
soup = BeautifulSoup(product_page_html, "lxml")

price = soup.select_one(selector=".a-price-whole")
value = float(price.text)

my_email = "testingpython4email@gmail.com"
password = "mzwv ozvf tncr apwf"

if value <= 90.0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        message = f"Price is below 91 rupees now buy it now!"
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Perfect price now!\n\n{message}"
        )
        