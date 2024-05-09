import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Arial Unicode MS'
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 读取CSV文件，并指定列名
df = pd.read_csv("shenzhen_2020_air.csv", encoding="utf-8",
                 names=["date", "zldj", "aqi", "pm25", "pm10", "so2", "no2", "co", "o3"])

# 绘制So2的变化趋势图，修改颜色为红色
df['so2'].plot(linestyle='-', marker='o', color='pink')  # 使用线性和标记点来绘制数据，颜色为红色

# 设置x轴和y轴的标签
plt.xlabel('时间')  # x轴应该是时间
plt.ylabel('二氧化硫(So2)浓度')  # y轴应该是二氧化硫的浓度

# 设置图表的标题
plt.title('二氧化硫(So2)变化趋势')

# 显示网格线（可选）
plt.grid(True)

# 显示图表
plt.show()
