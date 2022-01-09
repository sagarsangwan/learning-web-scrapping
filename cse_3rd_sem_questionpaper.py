import requests
from bs4 import BeautifulSoup
import mysql.connector


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'sagar',
    password = "password",
    database = "student-portal"
)
def get_all_subject_link():
    req = requests.get("https://brpaper.com/mdu/b-tech/cse")
    soup = BeautifulSoup(req.content, "html.parser")
    sem_link = []
    links = soup.select(".br-thumb")
    a = 0
    for link in links:
        a= a+1
        sem_link.append(link["href"])


    return sem_link

def get_question_paper_link(link):
    count  = 0
    subject_name = []
    q_links = []
    subject_desc = []
    year = []
    data = []
    for i in link:
        count = count+1
        req = requests.get(i)
        soup = BeautifulSoup(req.content, "html.parser")

        
        sub_name = soup.select('.br-thumb h6.text-dark span')

        for n in sub_name:
            subject_name.append(n.string)

        desc = soup.findAll("a", {"class": "br-thumb"})
        for d in desc:
            subject_desc.append(d["title"])
        for q in desc:
            q_links.append(q["href"])
        
        for i in range(0, len(subject_name)):
            data.append([subject_name[i], subject_desc[i]])


    return data


def upload_to_mysql(info):
    for n in info:
        cur = mydb.cursor()
        cur.execute("INSERT INTO subjects(subject_name, subject_desc) values(%s, %s)",(n[0], n[1]))
        

    mydb.commit()
    cur.close



# print(get_question_paper_link(get_all_subject_link()))
print(get_all_subject_link())