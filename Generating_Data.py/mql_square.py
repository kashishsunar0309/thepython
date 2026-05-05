import matplotlib.pyplot as plt
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.style.use('seaborn-v0_8')
#plt.style.use('ggplot')
#plt.style.use('classic')
#plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(2,4,s = 200)
#Set chart title and label axes.
#ax.plot(input_values,squares,linewidth = 3)
#ax.plot(squares,linewidth = 2)
#Set chart title and label axes.
ax.set_title("Square Numbers", fontsize = 15)
ax.set_xlabel("Value",fontsize = 15)
ax.set_ylabel("Square of Value", fontsize = 15)
#Set size of trick labels.
ax.tick_params(labelsize = 14)

plt.show()