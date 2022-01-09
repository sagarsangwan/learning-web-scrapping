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

# print(final_links(get_all_subject_link())[0].get("name"))

# for i in final_links(get_all_subject_link()):
    


# # def get_question_paper_link(link):
# subject_name = []
# qp_links = []
# subject_desc = []
# year_of_paper = []
# data = []

# req = requests.get("https://brpaper.com/mdu/b-tech/cse/1-2")
# soup = BeautifulSoup(req.content, "html.parser")
# item_card = soup.findAll("a", {"class": "br-thumb"})
# for i in item_card:
#     print((i.select(".br-thumb h6.text-dark span"))[0].string)

        
 

def upload_to_mysql(info):
    for n in info:
        cur = mydb.cursor()
        cur.execute(
            "INSERT INTO temp(name, sub_desc) values(%s, %s)", str((n.get("name"))), str(n.get("year")))

    mydb.commit()
    cur.close
    return"done"
upload_to_mysql(final_links(get_all_subject_link()))
print(upload_to_mysql(final_links(get_all_subject_link()))
)
print("after===========================")
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



# info= {}
# data = []
# subject_desc = []
# subject_name = []
# print("+++++====================================================================")
# req = requests.get("https://brpaper.com/mdu/b-tech/cse/3")
# print("====================================================================")
# soup = BeautifulSoup(req.content, "html.parser")

# item_card = soup.findAll("a", {"class": "br-thumb"})
# sub_name = soup.select('.br-thumb h6.text-dark span')

# for d in item_card:
#     print(d.select('h6 span')[0])
#     subject_desc.append(d["title"])
# for n in sub_name:
#     subject_name.append(n.string)
    
# for i in range(0, len((item_card))):
#     # b = info[subject_name[i]] = subject_desc[i]
#     suject = {
#         "desc": subject_desc[i],
#         "name": subject_name[i]
#     }
#     # print(b, subject)
#     data.append(suject)
# print(data)
# # print(b)