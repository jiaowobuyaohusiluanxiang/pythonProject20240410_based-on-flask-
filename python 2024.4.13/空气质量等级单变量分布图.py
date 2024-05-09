import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Arial Unicode MS'
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

df = pd.read_csv("shenzhen_2020_air.csv", encoding="utf-8",
                 names=["date", "zldj", "aqi", "pm25", "pm10", "so2", "no2", "co", "o3"],
                 skiprows=1)  # 跳过第一行

# 绘制空气质量等级单变量分布图
# 绘制以AQI为 x 轴，数据来源为aqi的计数图，修改颜色为蓝色
sns.countplot(x='zldj', data=df, color='blue')  # Change color to blue
# 设置标题为“空气质量等级单变量分布图”
plt.title("空气质量等级单变量分布图")
# 设置 x 轴标签为“空气质量等级”
plt.xlabel("空气质量等级")
# 设置 y 轴标签为“数量”
plt.ylabel("数量")
# 显示图像
plt.show()
