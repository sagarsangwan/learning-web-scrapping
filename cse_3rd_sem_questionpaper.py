import requests
from bs4 import BeautifulSoup

req = requests.get("https://brpaper.com/mdu/b-tech/cse/3")

soup = BeautifulSoup(req.content, "html.parser")

subject_name = []
q_links = []
sub_desc = []
year = []

name = soup.findAll("h6", {"class": "text-dark"})
# for n in name:
#     subject_name.append(span.text")
# print(subject_name)

desc = soup.findAll("a", {"class": "br-thumb"})
for d in desc:
    sub_desc.append(d["title"])



print(sub_desc)
# for i in desc:
#     print(i["title"])