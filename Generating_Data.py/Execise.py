import matplotlib.pyplot as plt 
#First 5
x_values = list(range(1,5000))
y_values = [x**3 for x in x_values]
fig, ax  = plt.subplots()
#for color execise
ax.scatter(x_values, y_values, color = 'red',s = 10)
plt.show()