from  bs4 import BeautifulSoup
import pymysql
import requests
import urllib3

req= requests.get("http://data.cma.cn/article/getServiceCase/cateId/9.html")
req.encoding="utf-8"
html=BeautifulSoup(req.text,"lxml")
lis = html.find_all("li",attrs={"class":"service_li"})
for v in lis:
    wrap= v.find("div", attrs={"class": "img_par"})
    url=wrap.find("img")["src"]
    title = v.find("div", attrs={"class": "case_name"}).text
    div = v.find("div", attrs={"class": "item"})
    ntype = div.find_all("div")[1].text
    time = div.find_all("div")[1].text
    description=v.find("div", attrs={"class": "case_achievement"}).text
    print("{},{},{},{},{}".format(url,title,ntype,time,description))
    conn = pymysql.connect(host="localhost",port=3306,user="root",passwd="lmy805727",db="sys",charset="utf8")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO news (url, title, ntype, time, des) VALUES (%s, %s, %s, %s, %s)", (url, title, ntype, time, description))
    conn.commit()
    cursor.close()
    conn.close()