import matplotlib.pyplot as plt
squares = [1,4,9,16,25]
fig, ax = plt.subplots()
ax.plot(squares,linewidth = 2)
#Set chart title and label axes.
ax.set_title("Square Numbers", fontsize = 15)
ax.set_xlabel("Value",fontsize = 15)
ax.set_ylabel("Square of Value", fontsize = 15)
#Set size of trick labels.
ax.tick_params(labelsize = 14)
plt.show()