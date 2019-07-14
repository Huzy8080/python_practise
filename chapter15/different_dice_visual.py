import pygal
from chapter15.die import Die

# 骰子列表
dies = []
# 创建一个6面的骰子
die_1 = Die()
dies.append(die_1)
# 创建一个10面的骰子
die_2 = Die(10)
dies.append(die_2)

# 搓几次骰子，将结果存入列表中
results = []
for roll_num in range(50000):
    result = 0
    for die in dies:
        result += die.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(len(dies), max_result + 1):
    frequencies.append(results.count(value))

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Result of rolling D6 and D10 dice 50000 times"
hist.x_labels = [str(value) for value in range(len(dies), max_result + 1)]
hist._x_title = "Result"
hist._y_title = "Frequency of Result"
hist.add('D6 + D10', frequencies)
hist.render_to_file('different_dice_visual.svg')
print(hist.x_labels)
print(frequencies)
