import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
x_value = list(range(1, 1001))
# y_values = [1, 4, 9, 16, 25]
y_values = [x ** 2 for x in x_value]

plt.scatter(x_value, y_values, s=20, edgecolors='none', c=y_values, cmap=plt.cm.Blues)
# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记大小
plt.tick_params(axis='both', which='major', labelsize=14)
# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
plt.show()
# 保存图片
# plt.savefig("squares_plot.png",bbox_inches='tight')