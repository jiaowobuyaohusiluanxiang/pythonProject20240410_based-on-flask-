
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# 读取数据到DataFrame中
df = pd.read_csv("shenzhen_2020_air.csv")

# 过滤掉包含非数字AQI值的行
df_numeric_aqi = df[df['AQI'].str.isnumeric()]

# 将AQI列转换为数值
df_numeric_aqi['AQI'] = pd.to_numeric(df_numeric_aqi['AQI'])

# 确定自变量和因变量
X = df_numeric_aqi.drop(columns=['AQI_Predict'])
y = df_numeric_aqi['AQI_Predict']

# 将数据集拆分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建线性回归模型
model = LinearRegression()

# 训练模型
model.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = model.predict(X_test)

# 计算均方根误差
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print("均方根误差:", rmse)

# 可视化预测值与真实值之间的比较
plt.scatter(y_test, y_pred)
plt.xlabel("真实值")
plt.ylabel("预测值")
plt.title("真实值 vs. 预测值")
plt.show()
