import pygal
from chapter15.die import Die

# 创建一个6面的骰子
die = Die()

# 搓几次骰子，将结果存入列表中
results = []
for roll_num in range(1000):
    results.append(die.roll())

# 分析结果
frequencies = []
for value in range(1, die.num_sides + 1):
    frequencies.append(results.count(value))

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Resule of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist._x_title = "Result"
hist._y_title = "Frequency of Result"
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
