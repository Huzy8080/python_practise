import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 获取最高气温
    dates, highs, lows = [], [], []
    for row in reader:
        high = row[8]
        if '' == high:
            high = 0
        highs.append(int(high))
        low = row[9]
        if '' == low:
            low = 0
        lows.append(int(low))

        dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # 设置图形格式
    plt.title("Daily high and low temperatures - 2018", fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
