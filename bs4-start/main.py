from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
response.raise_for_status()

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

story_titles = soup.select(selector=".titleline a")
titles = []
links = []
upvotes = []
for story in story_titles:
    if story.get("href")[:4] != "from":
        titles.append(story.getText())
        links.append(story.get("href"))

scores = soup.select(".score")
for score in scores:
    upvotes.append(int(score.getText().split()[0]))

largest_upvotes = max(upvotes)
index = upvotes.index(largest_upvotes)
print(titles[index])
print(links[index])

# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())
# print(soup.p)

# all_anchors = soup.find_all(name="a")
#
# for tag in all_anchors:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)

