import requests
import os
from twilio.rest import Client

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

parameters = {
    "appid": api_key,
    "lat": 12.971599,
    "lon": 77.594566,
    "cnt": 4

}
url = "https://api.openweathermap.org/data/2.5/forecast"
response = requests.get(url=url,params=parameters)
response.raise_for_status()

weather_data = response.json()
will_rain = False
for i in range(4):
    weather_id = weather_data["list"][i]["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring umbrella ☂️" ,
        from_='+19519728284',
        to='receiver mobile number'
    )
    print(message.status)
