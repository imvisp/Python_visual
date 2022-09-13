import csv
from email import header
from fileinput import filename
from datetime import datetime
from turtle import title
import matplotlib.pyplot as plt

filename = 'death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get dates, high and low temperature from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing the data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # print(highs)
    
# for index, colum_header in  enumerate(header_row):
#     print(index, colum_header)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha = 0.5)
ax.plot(dates, lows, c='blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format the plot.
title = " Daily high and low temperatures - 2018\ndeath valley"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (f)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()