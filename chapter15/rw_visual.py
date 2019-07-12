import matplotlib.pyplot as plt

from chapter15 import random_walk

while True:

    rw = random_walk.RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=5, c=rw.y_values, cmap=plt.cm.Blues)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='green', edgecolors='none', s=50)

    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
