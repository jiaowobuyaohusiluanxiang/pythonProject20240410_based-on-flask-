import pymysql

db=pymysql.connect(host="localhost",port=3306,user="root",passwd="lmy805727",db="sys",charset="utf8")
cur=db.cursor()
cur.execute("INSERT INTO uses (username, password) VALUES (%s, %s)", ('123', '123'))
db.commit()