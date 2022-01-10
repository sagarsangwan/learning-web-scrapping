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
    req = requests.get("https://brpaper.com/mdu/b-tech/me")
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
    subject_ids = []
    for n in info:
        cur = mydb.cursor()
        cur.execute("SELECT qp_name FROM question_paper")
        data = list(map(lambda x: x[0], cur.fetchall()))

        if n.get("name") in data:
            print("skipped-", n.get("name"))
        else:
            cur.execute("INSERT INTO question_paper(qp_name, link, year) values(%s, %s, %s)", (str((n.get("name"))), str(n.get("link")), str(n.get("year"))))
            cur.execute("SELECT LAST_INSERT_ID();")
            id =cur.fetchone()[0]
            cur.execute("INSERT INTO subjects(subject_name, subject_desc, question_papers) values(%s, %s, %s)", (str((n.get("name"))),str((n.get("desc"))), str(id)))
            cur.execute("SELECT LAST_INSERT_ID();")
            sub_id =cur.fetchone()[0]
            subject_ids.append(str(sub_id))
            cur.execute("INSERT INTO subjects_to_course(subject_id, course_ids) values(%s, %s)",(str(sub_id), "2"))
            print("inserted-", n.get("name"))

    if len(subject_ids) > 0: 
        cur.execute("INSERT INTO course_to_subjets(subjects_ids, course_id) VALUES (%s, %s) ON DUPLICATE KEY UPDATE subjects_ids=subjects_ids+%s", (",".join(subject_ids), "2", ",".join(subject_ids)))

    # cur.execute("UPDATE course_to_subjets SET subjects_ids = subjects_ids+ %s WHERE course_id = %s", (",".join(subject_ids), "1"))
    mydb.commit()
    cur.close()
    return"done"



upload_to_mysql(final_links(get_all_subject_link()))
print("after=================================")