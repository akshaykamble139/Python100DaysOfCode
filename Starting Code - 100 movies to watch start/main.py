import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
response.raise_for_status()

empire_html = response.text

soup = BeautifulSoup(empire_html, "html.parser")

movies = soup.find_all(name="h3", class_="title")

movies_list = []
for movie in movies[::-1]:
    movies_list.append(movie.text)
    print(movie.getText())

with open("movies.txt","w", encoding="utf-8") as file:
    for movie in movies_list:
        file.write(f"{movie}\n")