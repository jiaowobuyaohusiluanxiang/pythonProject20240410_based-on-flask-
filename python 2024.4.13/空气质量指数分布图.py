import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Arial Unicode MS'
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 读取CSV文件，并指定列名
df = pd.read_csv("shenzhen_2020_air.csv", encoding="utf-8",
                 names=["date", "zldj", "aqi", "pm25", "pm10", "so2", "no2", "co", "o3"])

# 空气质量定级函数
def get_level(aqi):
    if aqi < 35:
        return '优'
    elif aqi < 75:
        return '良'
    elif aqi < 150:
        return '轻度污染'
    elif aqi < 250:
        return '中度污染'
    elif aqi >= 250:
        return '重度污染'  # 注意：这里应该是'重度污染'而不是'高度污染'

# 给原始数据添加新列 'level'
df['level'] = df['aqi'].apply(get_level)

# 统计各种空气质量的比例
bj_level = df.groupby('level')['aqi'].count() / len(df)

# 按照出现次数降序排序，这样标签和饼图的数据可以对应起来
bj_level = bj_level.sort_values(ascending=False)

# 画图
labels = bj_level.index.tolist()
colors = ['lightgreen', 'skyblue', 'orange', 'lightcoral', 'salmon']  # Define colors
plt.pie(bj_level, labels=labels, autopct='%.2f%%', colors=colors)  # Use colors parameter
plt.title('空气质量指数分布')
plt.axis('equal')  # 使饼图保持圆形
plt.show()
