import pygal
from chapter15.die import Die

# 创建一个6面的骰子
die_1 = Die()
die_2 = Die()

# 搓几次骰子，将结果存入列表中
results = []
for roll_num in range(1000):
    results.append(die_1.roll() + die_2.roll())

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequencies.append(results.count(value))

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Result of rolling two D6 dice 1000 times"
hist.x_labels = [str(value) for value in range(2, max_result + 1)]
hist._x_title = "Result"
hist._y_title = "Frequency of Result"
hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
print(hist.x_labels)
print(frequencies)
