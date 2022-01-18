import matplotlib.pyplot as plt
import numpy as np

coords = {"coords{}".format(i): [] for i in range(4)}

coords["coords1"] = [(4, y) for y in np.arange(-4, 16, 0.01)]
coords["coords2"] = [(x, 2 * x + 8) for x in np.arange(4, 6, 0.01)]
coords["coords3"] = [(x, 20) for x in np.arange(6, 15, 0.01)]
coords["coords4"] = [(x, -(2 / 3) * x + 30) for x in np.arange(15, 18, 0.01)]
coords["coords5"] = [(x, -2 * x + 54) for x in np.arange(18, 19, 0.01)]
coords["coords6"] = [((y - 282) / (-14), y) for y in np.arange(14.923, 16, 0.01)]

for line in coords:
    x = []
    y = []
    for coord in coords[line]:
        x.append(coord[0])
        y.append(coord[1])
    plt.plot(x, y)

plt.show()

"""


x5 = [coord[0] for coord in coords5]
y5 = [coord[1] for coord in coords5]


x6 = [coord[0] for coord in coords6]
y6 = [coord[1] for coord in coords6]

coords7 = [(x, -14 * x + 282) for x in np.arange(4, 11.333, 0.1)]
x7 = [coord[0] for coord in coords7]
y7 = [coord[1] for coord in coords7]

coords8 = [(x, 8 * x - 155) for x in np.arange(2, 4, 0.1)]
x8 = [coord[0] for coord in coords8]
y8 = [coord[1] for coord in coords8]

"""
