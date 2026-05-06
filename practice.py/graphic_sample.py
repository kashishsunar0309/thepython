import matplotlib.pyplot as plt
multi_2 = [40,40,40,40,40,40,40,40,40,40,40,40]
multi_3 = [70,5,80,4,75,3,77,2,65,12,4.5,100]
cross = [0,12,25,32,38,45,55,74,78,82,85,90]
fix, ax = plt.subplots()
ax.plot(multi_2)
ax.plot(multi_3)
ax.plot(cross)
plt.show()