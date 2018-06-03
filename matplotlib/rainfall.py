import csv
from datetime import datetime

import requests
from matplotlib import pyplot as plt

# Get dates and rainfall data from data file.
# Rainfall data is in column 19.
url = 'https://raw.githubusercontent.com/ehmatthes/pcc/gh-pages/resources/sitka_rainfall_2015.csv'
filename = 'data/sitka_rainfall_2015_url.csv'

req = requests.get(url)  # 1
# 将数据写入文件
with open(filename, 'w') as f:
    f.write(req.text)
    f.close()

# from io import StringIO
#
# # 封装成StringIO对象
# data = urlopen(url).read().decode('ascii', 'ignore')
# dataFile = StringIO(data)
# csvReader = csv.reader(dataFile)

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, rainfalls, totals = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            rainfall = float(row[19])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            rainfalls.append(rainfall)
            if totals:
                totals.append(totals[-1] + rainfall)
            else:
                totals.append(rainfall)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))

plt.plot(dates, rainfalls, c='blue', alpha=0.5)
plt.fill_between(dates, rainfalls, facecolor='blue', alpha=0.2)

plt.plot(dates, totals, c='blue', alpha=0.75)
plt.fill_between(dates, totals, facecolor='blue', alpha=0.05)

# Format plot.
title = "Daily rainfall amounts and cumulative rainfall - 2015\nSitka, AK"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall (in)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
