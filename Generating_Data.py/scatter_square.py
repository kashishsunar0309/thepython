import matplotlib.pyplot as plt
x_values = range(1,1001)
y_values = [x**2 for x in x_values]
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.scatter(x_values,y_values, s= 10)
#Set the range for each axis.
ax.set_title("Square Numbers", fontsize = 15)
ax.set_xlabel("Value",fontsize = 15)
ax.set_ylabel("Square of Value", fontsize = 15)
#Set size of trick labels.
ax.tick_params(labelsize = 14)
ax.axis([0, 1100, 0, 1_100_000])# [xmin, xmax, ymin, ymax]
plt.show()