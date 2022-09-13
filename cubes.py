import matplotlib.pyplot as plt

# using lists
x_values = [1,2,3,4,5]
y_values = [1,8,27,64,125]

# using loop
x_values = range(1, 1000)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# set chart title and lable axes.
ax.set_title("Cube Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Cube of Value", fontsize = 14)

#set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()