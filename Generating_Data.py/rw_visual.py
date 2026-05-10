import matplotlib.pyplot as plt
from random_walk import RandomWalk
#Keeping making new walks,as long as the program is active.
while True:
    rw = RandomWalk()
    rw.fill_walk()
    fig, ax = plt.subplots()
    plt.style.use('classic')
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c= point_numbers, cmap='Wistia',
               edgecolors = 'none',s=15)
    ax.scatter(rw.x_values, rw.y_values, s=15)
    ax.set_aspect('equal')
    plt.show()
    keep_running = input("Make another Walk? (y/n): ")
    if keep_running == 'n':
        break