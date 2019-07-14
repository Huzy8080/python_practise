import matplotlib.pyplot as plt


from chapter15 import random_walk

while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = random_walk.RandomWalk(50000)
    rw.fill_walk()
    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10, 6))
    # 绘制点并将图形显示出来
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, s=1, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none')
    # 突出起点和终点
    plt.scatter(0, 0, c='red', edgecolors='none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='green', edgecolors='none', s=50)
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    # 显示
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
