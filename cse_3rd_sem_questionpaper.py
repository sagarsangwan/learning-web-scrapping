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
    a = 0
    for link in links:
        sem_link.append(link["href"])

    return sem_link


def get_question_paper_link(link):
    subject_name = []
    qp_links = []
    subject_desc = []
    year_of_paper = []
    data = []
    for i in link:
        req = requests.get(i)
        soup = BeautifulSoup(req.content, "html.parser")

        sub_name = soup.select('.br-thumb h6.text-dark span')

        for n in sub_name:
            subject_name.append(n.string)

        desc = soup.findAll("a", {"class": "br-thumb"})
        for d in desc:
            subject_desc.append(d["title"])
        for q in desc:
            qp_links.append(q["href"])

        for i in range(0, len(subject_name)):
            data.append([subject_name[i], subject_desc[i]])

    return data


def upload_to_mysql(info):
    for n in info:
        cur = mydb.cursor()
        cur.execute(
            "INSERT INTO subjects(subject_name, subject_desc) values(%s, %s)", (n[0], n[1]))

    mydb.commit()
    cur.close


# print(get_question_paper_link(get_all_subject_link()))
# print(get_all_subject_link())


# def get_question_paper_link1(link):
#     subject_name = {}
#     qp_links = {}
#     subject_desc = {}
#     year_of_paper = {}
#     data = []

#     req = requests.get(link)
#     soup = BeautifulSoup(req.content, "html.parser")


#     desc = soup.findAll("a", {"class": "br-thumb"})
#     for d in desc:
#         subject_desc.append(d["title"])
#     for q in desc:
#         qp_links.append(q["href"])

#     for i in range(0, len(subject_name)):
#         data.append([subject_name[i], subject_desc[i]])

#     return data

# print(get_question_paper_link1("https://brpaper.com/mdu/b-tech/cse/1-2"))



info= {}
data = []
subject_desc = []
subject_name = []
print("+++++====================================================================")
req = requests.get("https://brpaper.com/mdu/b-tech/cse/3")
print("====================================================================")
soup = BeautifulSoup(req.content, "html.parser")

item_card = soup.findAll("a", {"class": "br-thumb"})
sub_name = soup.select('.br-thumb h6.text-dark span')

for d in item_card:
    print(d.select('h6 span')[0])
    subject_desc.append(d["title"])
for n in sub_name:
    subject_name.append(n.string)
    
for i in range(0, len((item_card))):
    # b = info[subject_name[i]] = subject_desc[i]
    suject = {
        "desc": subject_desc[i],
        "name": subject_name[i]
    }
    # print(b, subject)
    data.append(suject)
print(data)
# print(b)