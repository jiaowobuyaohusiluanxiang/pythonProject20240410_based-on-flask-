import requests
from bs4 import BeautifulSoup
def fun(city,year):
    for i in range(1,13):
        m=""
        if i<10:
            m="0"+str(i)
        else:
            m=str(i)

        url = "http://www.tianqihoubao.com/aqi/" + city + "-" + str(year) + m + ".html"
    req=requests.get(url)
    html=BeautifulSoup(req.text,"lxml")
    tab=html.find("table")
    tr=tab.find_all("tr")
    for i in tr[1:]:
        td=i.find_all("td")
        time=str(td[0].text).split()
        zldj=str(td[1].text).split()
        aqi=str(td[2].text).split()
        pm25=str(td[4].text).split()
        pm10=str(td[5].text).split()
        so2=str(td[6].text).split()
        no2=str(td[7].text).split()
        co=str(td[8].text).split()
        o3=str(td[9].text).split()
        with open(city + "_" + str(year) + ".csv", "a+", encoding="utf-8") as file:
            file.write(
                ','.join(time) + "," + ','.join(zldj) + "," + ','.join(aqi) + "," + ','.join(pm25) + "," + ','.join(
                    pm10) + "," + ','.join(so2) + "," + ','.join(no2) + "," + ','.join(co) + "," + ','.join(o3) + "\n")

fun("shenzhen",2020)
