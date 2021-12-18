import requests
from bs4 import BeautifulSoup

req = requests.get("https://sagarsangwan.herokuapp.com/")
soup = BeautifulSoup(req.content, "html.parser")

# print(soup.prettify())
# print(soup.get_text())
# print(soup.title.string)
print(soup.find_all("a"))
# print(soup.p)
# print(soup.find("link"))

link = soup.find_all("a")
for i in link:
    print(i.get("href"))
