import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 8, 27, 64, 125]

x_values = list(range(1, 5001))
y_values = [x ** 3 for x in x_values]

plt.scatter(x_values, y_values, s=20, c=y_values, cmap=plt.cm.Blues)
# 设置图表标题，并给坐标轴加上标签
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.axis([0, 5001, 0, 130000000000])
plt.show()
