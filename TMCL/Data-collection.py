from matplotlib import pyplot as plt
import pandas as pd
import random
from itertools import count
from matplotlib.animation import FuncAnimation
from TMCL import Scripts

'''x = [1, 2, 3]
y = [1, 4, 9]

plt.plot(x, y)
plt.show()'''

x_value = []
y_value = []

index = count()


def animate(i):
    x_value.append(next(index))
    y_value.append(random.randint(0, 5))
    plt.cla
    plt.plot(x_value, y_value)

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()

