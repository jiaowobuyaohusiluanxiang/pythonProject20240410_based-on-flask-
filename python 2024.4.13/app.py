from flask import Flask, render_template, request, session, redirect, url_for
import pymysql
import requests
#from bs4 import BeautifulSoup
import pandas as pd
from pyecharts.charts import Line,Bar,Pie,Funnel
from pyecharts import options as opts

app=Flask(__name__)
db=pymysql.connect(host="localhost",port=3306,user="root",passwd="lmy805727",db="sys",charset="utf8")
cur=db.cursor()
df = pd.read_csv("shenzhen_2020_air.csv",encoding="utf-8",names=["data","zldj","aqi","pm25","pm10","so2","no2","co","o3"])

@app.route('/datas')
def datas():
    df=pd.read_csv("shenzhen_2020_air.csv",encoding="utf-8",names=["data","zldj","aqi","pm25","pm10","so2", "no2","co","o3"])
    arr=[]
    for index,row in df.iterrows():
        dic={}
        dic["date"]=row[0]
        dic["zldj"]=row[1]
        dic["aqi"]=row[2]
        dic["pm25"]=row[3]
        dic["pm10"]=row[4]
        dic["so2"]=row[5]
        dic["no2"]=row[6]
        dic["co"]=row[7]
        dic["o3"]=row[8]
        arr.append(dic)

    return render_template("about.html",data=arr)

def is_logged_in():
    return 'username' in session

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/services.html')
def services():
    return render_template('services.html')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/register.html', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    # 检查用户名是否已存在
    cur.execute("SELECT * FROM uses WHERE username = %s", (username))
    existing_user = cur.fetchone()
    if existing_user:
        return "Username already exists! Please choose a different username."

    # 将新用户信息插入到数据库中
    try:
        cur.execute("INSERT INTO uses (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
    except Exception as e:
        db.rollback()
        return f"Error occurred: {str(e)}"

    # 注册成功后自动登录
    return redirect(url_for('login_page'))

@app.route('/index.html')
def index_page():
        # 登录成功，重定向到主页
        cur.execute("select * from lmy")
        data = cur.fetchall()
        return render_template("index.html", data=data)

@app.route('/login')
def login_page():
    return render_template('login.html')



@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # 验证用户名和密码
    cur.execute("SELECT * FROM uses WHERE username = %s AND password = %s", (username, password))
    user = cur.fetchone()
    if user:
      return redirect(url_for('index_page'))

    else:
        # 登录失败，重定向回登录页面
        return redirect(url_for('/'))

@app.route('/pm_year')#线形图
def pm_year():
    df = pd.read_csv("shenzhen_2020_air.csv", encoding="utf-8",
                     names=["date", "zldj", "aqi", "pm2.5", "pm10", "so2", "no2", "co", "o3"])
    x=df["date"]
    y1=df["pm2.5"]
    y2=df["pm10"]
    c = (
        Line(init_opts=opts.InitOpts(bg_color="pink"))
        .add_xaxis([str(date) for date in df["date"].tolist()])
        .add_yaxis("PM2.5", df["pm2.5"].tolist())
        .add_yaxis("PM10", df["pm10"].tolist())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2020年深圳PM值的全年数据分析", pos_left="center", pos_top="20px", title_textstyle_opts={"color": "black"}),
            legend_opts=opts.LegendOpts(pos_right="100px", pos_top="20px"))
        )
    return render_template("contact.html", myechart=c.render_embed())

@app.route('/so_month')#柱状图
def so_mouth():
    df = pd.read_csv("shenzhen_2020_air.csv", encoding="utf-8",
                     names=["date", "zldj", "aqi", "pm25", "pm10", "so2", "no2", "co", "o3"])
    v=pd.to_datetime(df['date'],format="%Y-%m-%d")
    df.index=v
    def fun(x):
        return x.month
    m=df.groupby(fun)
    y1=m["so2"].mean().round(2)
    y2 = m["no2"].mean().round(2)
    x= [str(i)+"月" for i in range(1,13)]

    c = (
       Bar(init_opts=opts.InitOpts(bg_color="#E6E6E6"))
        .add_xaxis(list(x))
        .add_yaxis("PM2.5",list(y1))
        .add_yaxis("PM10",list(y2))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2020年深圳每月的的so2平均值分析", pos_left="center", pos_top="20px", title_textstyle_opts={"color": "black"}),
            legend_opts=opts.LegendOpts(pos_right="100px", pos_top="20px"))
    )

    return render_template("portfolio.html", myechart=c.render_embed())


@app.route('/zldj_year')#饼状图
def zldj_year():
    df = pd.read_csv("shenzhen_2020_air.csv", encoding="utf-8", names=["date", "zldj", "aqi", "pm25", "pm10", "so2", "no2","co", "o3"])
    m = df.groupby("zldj").count()

    c = (
        Pie(init_opts=opts.InitOpts(bg_color="#E6E6E6"))
        .add("空气质量等级", [list(z) for z in zip(m.index, m["date"])])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2020年深圳全年空气质量总和分析", pos_left="center", pos_top="20px", title_textstyle_opts={"color": "black"}),
            legend_opts=opts.LegendOpts(pos_right="100px", pos_top="20px")
        )
    )

    return render_template("portfolio.html", myechart=c.render_embed())

if __name__=='__main__':
    app.run(debug=True)