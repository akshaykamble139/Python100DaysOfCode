STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import requests
import datetime
from twilio.rest import Client
import os


STOCK_API_KEY = "LUTR7CWG7ENTZ0TB"
NEWS_API_KEY = "49116e8de9c14cb99367c0fecba2520e"

TWILIO_SID = os.environ['TWILIO_SID']
TWILIO_AUTH_KEY = os.environ['TWILIO_AUTH_KEY']

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_parameters ={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
response = requests.get("https://www.alphavantage.co/query", params=stock_parameters)
response.raise_for_status()

data = response.json()["Time Series (Daily)"]
now = datetime.datetime.now()
prev = datetime.timedelta(days=-1)
prev_day_time = prev + now
day_before_prev_time = now + prev + prev

yesterday = prev_day_time.strftime("%Y-%m-%d")
day_before_yesterday = day_before_prev_time.strftime("%Y-%m-%d")

stock_price_yesterday = float(data[yesterday]["4. close"])
stock_price_day_before_yesterday = float(data[day_before_yesterday]["4. close"])

diff_percent = round((stock_price_day_before_yesterday - stock_price_yesterday)/ stock_price_day_before_yesterday * 100,2)

if abs(diff_percent) >= 1:
    up_down = None
    if diff_percent>0:
        up_down = "🔺"
    else:
        up_down = "🔻"

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

    news_parameters = {
        "q": "Tesla",
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get("https://newsapi.org/v2/everything",params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"][:3]
    print(news_data)
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
    articles_list = [f"{COMPANY_NAME}: {up_down}{abs(diff_percent)}%\nHeadline: {article['title']}. \nBrief: {article['description']} " for article in news_data]
    client = Client(TWILIO_SID,TWILIO_AUTH_KEY)
    for article in articles_list:
        message = client.messages.create(
                 body=article,
                 from_='+19519728284',
                 to='Your mobile number'
             )
        print(message.status)
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

