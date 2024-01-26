import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "akshay139"
TOKEN = "g85f7ofd6rjguoji67rdtf"
GRAPH_ID = "graph01"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint,json=user_params)
# response.raise_for_status()
#
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "problems",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# today = datetime.now().strftime("%Y%m%d")
today = datetime.now().strftime("%Y%m%d")
pixel_data = {
    "date": today,
    "quantity": "5",
}

response = requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
print(response.text)

# update_pixel_endpoint = f"{pixel_creation_endpoint}/{today}"
# response = requests.put(url=update_pixel_endpoint,json=pixel_data,headers=headers)
# print(response.text)

# response = requests.delete(url=update_pixel_endpoint,headers=headers)
# print(response.text)