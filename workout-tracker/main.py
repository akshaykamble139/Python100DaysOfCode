import requests
from datetime import datetime
import os


nutritionix_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
SHEETY_AUTH_HEADER_KEY = os.environ["SHEETY_AUTH_HEADER_KEY"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

user_input = input("Tell me what exercises you did: ")
exercise_parameters = {
    "query": user_input
}
response = requests.post(url=nutritionix_exercise_endpoint, headers=headers, json=exercise_parameters)
data = response.json()["exercises"]

sheety_auth_header = {
    "Authorization": f"Bearer {SHEETY_AUTH_HEADER_KEY}"
}
for record in data:
    sheety_parameters = {
        "workout": {
            "exercise": record["name"].title(),
            "duration": record["duration_min"],
            "calories": record["nf_calories"],
            "date": date,
            "time": time,
        }
    }

    sheets_response = requests.post(url=SHEETY_ENDPOINT,json=sheety_parameters, headers=sheety_auth_header)
    print(sheets_response.json())
