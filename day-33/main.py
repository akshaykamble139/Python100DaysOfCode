import requests
import datetime as dt
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# response.raise_for_status()
# data = response.json()
# print(data["iss_position"])

MY_LAT = 51.507351
MY_LONG = -0.127758

paramters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json",params=paramters)
response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]

now = dt.datetime.now()

print(sunrise)
print(sunset)
# print(now)