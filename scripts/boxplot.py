import os
import numpy as np
import matplotlib.pyplot as plt

naive = []
opti = []

t = 8
k = 512
lamda = 4096
ww = [-2, -1, 0, 2, 3]


labels = {
    0: "Naive",
    -1: "Parallel",
    -2: "Parallel Diff",
    1: "W=1",
    2: "W=2",
    3: "W=3",
}

titles = {
    1: "Min",
    2: "Mean",
    3: "Median",
    4: "Max"
}

functions = {
    1: np.min,
    2: np.mean,
    3: np.median,
    4: np.max
}

names = ["Parallel Diff", "Parallel", "Naive", "W=2", "W=3"]


time_plot = []

for w in ww:
    f = open("result/" + str(t) + "_" + str(lamda) +
             "_" + str(k) + "_" + str(w) + ".csv")
    verif_time = []

    for line in f:
        verif_time.append(float(line.split(';')[3]))
    print(len(verif_time))
    time_plot.append(verif_time)


minor_ticks = np.arange(0, 1, 1)

plt.boxplot(time_plot)
plt.yscale("log")
plt.grid(True, axis="y", which="both", ls="-")
plt.xticks([1, 2, 3, 4, 5], names)


plt.title("K=1024, λ=4096, 50 iterations")
plt.savefig("1024.pdf")
plt.show()
