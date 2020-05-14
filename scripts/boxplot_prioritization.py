import os
import numpy as np
import matplotlib.pyplot as plt

naive = []
opti = []

t = 8
k = 256
lamda = 4096
ww = [-1, 0, 2, 3]


labels = {
    0: "Naive",
    -1: "Parallel",
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

prio = "_no_prioritization"
pp = ["_prioritization", "_no_prioritization", "_under_prioritization"]

names = ["Highest", "Default", "Least"]
w_names = {-1: "Parallel", 0: "Naive", 2: "W=2", 3: "W=3"}

figure = plt.figure()

i = 1
for w in ww:
    ax = figure.add_subplot(2, 2, i)
    i += 1

    time_plot = []

    for prio in pp:
        f = open("result" + prio + "/" + str(t) + "_" + str(lamda) +
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
    plt.xticks([1, 2, 3, 4], names)
    ax.title.set_text(w_names[w])

figure.suptitle('Over 100 iterations for each boxplot, λ=4096, k=256')
plt.savefig(str(lamda) + "_C++_boxplot" + ".pdf")
plt.show()
