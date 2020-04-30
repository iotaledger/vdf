import os
import numpy as np
import matplotlib.pyplot as plt

naive = []
opti = []

t = 8
kk = [8, 9, 10]
kk_values = [2**k for k in kk]
kk_print = [2**(k + 1) for k in kk]
lamda = 4096
ww = [-1, 0, 2, 3]
zero = [0 for k in kk]


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

figure = plt.figure()

for i in range(1, 5):
    plt.subplot(2, 2, i)
    for w in ww:
        verif_time = []
        for k in kk_values:
            file = open("result/" + str(t) + "_" + str(lamda) +
                        "_" + str(k) + "_" + str(w) + ".csv")

            temp_array = []

            for line in file:
                line_array = line.split(";")
                temp_array.append(float(line_array[3]))

            verif_time.append(functions[i](temp_array))

        plt.plot(kk_print, verif_time, marker='o', label=labels[w])

    plt.xticks(kk_print)

    plt.legend()
    plt.title(titles[i])
plt.savefig(str(lamda) + "_C++_variation.pdf")
figure.suptitle("Variation time for λ=" + str(lamda) + " in C++ interface")
plt.show()
