import requests
from bs4 import BeautifulSoup

req = requests.get("https://sagarsangwan.herokuapp.com/")
soup = BeautifulSoup(req.content, "html.parser")

print(soup.prettify())
print(soup.get_text())

