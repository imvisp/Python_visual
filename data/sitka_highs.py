import csv
from fileinput import filename
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # Get dates and high temperature from this file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

    # print(highs)
    
# for index, colum_header in  enumerate(header_row):
#     print(index, colum_header)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format the plot.
plt.title(" Daily high temperatures, july 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate
plt.ylabel("Temperature (f)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()