import requests
from bs4 import BeautifulSoup
import mysql.connector


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = "admin",
    database = "users"
)

req = requests.get("https://brpaper.com/mdu/b-tech/cse/3")

soup = BeautifulSoup(req.content, "html.parser")

subject_name = []
q_links = []
subject_desc = []
year = []
sub_name = soup.select('.br-thumb h6.text-dark span')

for n in sub_name:
    subject_name.append(n.string)

desc = soup.findAll("a", {"class": "br-thumb"})
for d in desc:
    subject_desc.append(d["title"])
for q in desc:
    q_links.append(q["href"])
info = []
for i in range(0, len(subject_name)):
    info.append([subject_name[i], subject_desc[i]])

print(info)


# for n in info:
#     cur = mydb.cursor()
#     cur.execute("INSERT INTO subjects(subject_name, subject_desc) values(%s, %s)",(n[0], n[1]))
    

# mydb.commit()
# cur.close