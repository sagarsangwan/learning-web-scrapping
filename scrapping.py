import requests
from bs4 import BeautifulSoup



# loading webpage content by using request 
req = requests.get("https://brpaper.com/mdu/b-tech/cse/3")

# converting to a beautifulsoup object
soup = BeautifulSoup(req.content, "html.parser")

# to print or view html = print(soup), use soup.prettify() to get littlebit beautiful html
# print(soup.prettify())

link = soup.findAll('a', {"class": "br-thumb"})
b= 0
for a in link:
    b=b+1
    print(a['href'])

# print(link)
# print("sagar")
print(b)


# link = soup.find_all("a", class_ = "brpaper-courses")
# # for i in link:
# #     print(i.get("href"))
# print(link)









# print()
# print(soup.get_text())
# print(soup.title.string)
# print(soup.find_all("a"))
# print(soup.p)
# print(soup.find("link"))