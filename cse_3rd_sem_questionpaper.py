import requests
from bs4 import BeautifulSoup
import mysql.connector


mydb = mysql.connector.connect(
    host='localhost',
    user='sagar',
    password="password",
    database="student-portal"
)


def get_all_subject_link():
    req = requests.get("https://brpaper.com/mdu/b-tech/cse")
    soup = BeautifulSoup(req.content, "html.parser")
    sem_link = []
    links = soup.select(".br-thumb")
    for link in links:
        sem_link.append(link["href"])

    return sem_link

def final_links(links):
    data = []
    for link in links:
        req = requests.get(link)
        soup = BeautifulSoup(req.content, "html.parser")
        item_card = soup.findAll("a", {"class": "br-thumb"})
        
        for i in item_card:
            name = (i.select(".br-thumb h6.text-dark span"))[0].string
            desc = i["title"]
            year = i.select(".overlay strong.text-white")[0].string
            link = i["href"]
            dic = {
                "name": name,
                "desc": desc,
                "year": year,
                "link": link,
            }
            data.append((dic))
        
    return data 
print("before===============")

        
 

def upload_to_mysql(info):
    for n in info:
        cur = mydb.cursor()
        cur.execute(
            "INSERT INTO temp(name, sub_desc) values(%s, %s)", (str((n.get("name"))), str(n.get("year"))))

    mydb.commit()
    cur.close()
    return"done"

upload_to_mysql(final_links(get_all_subject_link()))
print("after=================================")