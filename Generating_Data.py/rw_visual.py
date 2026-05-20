import matplotlib.pyplot as plt
from random_walk import RandomWalk
#Keeping making new walks,as long as the program is active.
"""while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()
    #This two are option fig, ax ....{
    #fig, ax = plt.subplots(figsize = (15,9))
    #fig, ax = plt.subplots(figsize = (15,9),dpi = 128)}'''
    fig, ax = plt.subplots()
    plt.style.use('classic')
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c= point_numbers, cmap='Wistia',
               edgecolors = 'none',s=1)
    ax.scatter(rw.x_values, rw.y_values, s=15)
    ax.set_aspect('equal')
    #Emphasize the first and last points.
    ax.scatter(0,0, c= 'green', edgecolors = 'none', s = 100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',
               edgecolors = 'none',s = 100)
    #Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another Walk? (y/n): ")
    if keep_running == 'n':
        break
"""
#15-3:
#ex 15 execise.
while True:
    rw = RandomWalk(5_000)
    rw.fill_walk()
    fig, ax = plt.subplots(figsize = (15,9))
    ax.plot(rw.x_values, rw.y_values,linewidth =1)
    ax.set_aspect('equal')
    plt.show()
    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break