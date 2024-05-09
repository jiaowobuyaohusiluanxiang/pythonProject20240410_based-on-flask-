import pd
from flask import Flask, render_template, redirect, url_for, request, session
import pymysql
import pandas as pd
from pyecharts.charts import Line, Bar, Pie
from pyecharts import options as opts
from pyecharts.charts import Line

app = Flask(__name__)
db = pymysql.connect(host="localhost", port=3306, user="root", passwd="lmy805727", db="sys", charset="utf8")
cur = db.cursor()
df = pd.read_csv("shenzhen_2020_air.csv", encoding="utf-8",
                 names=["date", "zldj", "aqi", "pm25", "pm10", "so2", "no2", "co", "o3"])


def is_logged_in():
    return 'username' in session


@app.route('/')
def home():
    if not is_logged_in():
        return redirect(url_for('login_page'))
    return render_template("index.html", data=data)


@app.route('/about.html')
def about():
    arr = []
    for index, row in df.iterrows():
        dic = {}
        dic["data"] = row[0]
        dic["zldj"] = row[1]
        dic["aqi"] = row[2]
        dic["pm25"] = row[3]
        dic["pm10"] = row[4]
        dic["so2"] = row[5]
        dic["no2"] = row[6]
        dic["co"] = row[7]
        dic["o3"] = row[8]
        arr.append(dic)
    return render_template('about.html', data=arr)


@app.route('/services.html')
def so_month():
    df = pd.read_csv("shenzhen_2020_air.csv", encoding="utf-8",
                     names=["date", "zldj", "aqi", "pm25", "pm10", "so2", "no2", "co", "o3"])
    v = pd.to_datetime(df["date"], format="%Y-%m-%d")
    df.index = v

    m = df.groupby(df.index.month)
    y1 = m["so2"].mean().round(2)
    y2 = m["no2"].mean().round(2)  # 假设你想要 no2 的平均值
    x = [str(i) + "月" for i in range(1, 13)]

    c = (
        Bar(init_opts=opts.InitOpts(bg_color="#E6E6E6"))
        .add_xaxis(list(x))
        .add_yaxis("SO2", list(y1))
        .add_yaxis("NO2", list(y2))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2020年深圳每月的SO2与No2平均值分析", pos_left="center", pos_top="20px",
                                      title_textstyle_opts={"color": "black"}),
            legend_opts=opts.LegendOpts(pos_right="100px", pos_top="20px")
        )
    )

