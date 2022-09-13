from shutil import which
import matplotlib.pyplot as plt

# using list
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 6, 16, 25]

#usnig for loop
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
#this is using loop format.
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#active when use list format.
#ax.scatter(x_values, y_values, s=100)

# set chart title and lable axes.
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

# set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

#set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()