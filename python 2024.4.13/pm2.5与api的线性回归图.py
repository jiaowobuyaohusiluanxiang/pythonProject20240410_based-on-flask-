import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Arial Unicode MS'
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

df = pd.read_csv("shenzhen_2020_air.csv", encoding="utf-8",
                 names=["data", "zldj", "aqi", "pm25", "pm10", "so2", "no2", "co", "o3"],
                 skiprows=1)  # 跳过第一行

# 绘制PM2.5与AQI的线性回归拟合图
# 调用seaborn库的regplot函数，将PM2.5含量（ppm）作为x轴，AQI作为y轴，数据源为aqi
sn.regplot(x='pm25',  y='aqi',  data=df, color='blue')  # Change color to green

# 设定图表标题为'PM2.5与AQI的线性回归拟合图'
plt.title('PM2.5与AQI的线性回归拟合图')
# 设定图表x轴标签为'PM2.5含量（ppm）'
plt.xlabel('PM2.5含量（ppm）')
# 设定图表y轴标签为'AQI'
plt.ylabel('AQI')
# 显示图表
plt.show()
