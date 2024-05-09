import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Arial Unicode MS'
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

df = pd.read_csv("shenzhen_2020_air.csv", encoding="utf-8",
                 names=["date", "zldj", "aqi", "pm25", "pm10", "so2", "no2", "co", "o3"],
                 skiprows=1)  # 跳过第一行

# 绘制 aqi 和 pm2.5 的关系散点图
# 设置图像尺寸
plt.figure(figsize=(15, 10))
# 绘制散点图，横坐标为空气质量等级数据的第二列，纵坐标为AQI数据的第四列
plt.scatter(df[df.columns[1]], df[df.columns[3]], color='blue')  # Change color to orange
# 设置横轴标签为'空气等级'，字体大小为20
plt.xlabel('空气等级', fontsize=20)
# 设置纵轴标签为'AQI'，字体大小为20
plt.ylabel('AQI', fontsize=20)
# 设置图像标题为'空气质量等级分类散点图'，字体大小为25
plt.title('空气质量等级分类散点图', fontsize=25)
# 显示图像
plt.show()
