from importlib import import_module
import matplotlib.pyplot as plt

from random_walk import Randomwalk

# keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = Randomwalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 8))
    points_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=points_numbers, cmap=plt.cm.Blues, edgecolors='None', s=1)

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # remove the exes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()

    keep_running = input("Want to make another walk ? (y/n): ")
    if keep_running == 'n':
        break