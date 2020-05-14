import os
import numpy as np
import matplotlib.pyplot as plt

naive = []
opti = []

t = 8
kk = [6, 7, 8, 9, 10]
kk_values = [2**k for k in kk]
kk_print = [2**(k + 1) for k in kk]
lamda = 4096
ww = [-1, 2, 3]
zero = [0 for k in kk]


labels = {
    0: "Naive",
    -1: "Parallel",
    1: "W=1",
    2: "W=2",
    3: "W=3",
}

metric = np.mean

naive_time = []

for k in kk_values:
    file = open("result/" + str(t) + "_" + str(lamda) +
                "_" + str(k) + "_" + str(0) + ".csv")

    temp_array = []

    for line in file:
        line_array = line.split(";")
        temp_array.append(float(line_array[3]))

    naive_time.append(metric(temp_array))

plt.plot(kk_print, naive_time, marker='o', label="Naive")

for w in ww:
    verif_time = []
    for k in kk_values:
        file = open("result/" + str(t) + "_" + str(lamda) +
                    "_" + str(k) + "_" + str(w) + ".csv")

        temp_array = []

        for line in file:
            line_array = line.split(";")
            temp_array.append(float(line_array[3]))

        verif_time.append(metric(temp_array))

    plt.plot(kk_print, verif_time, marker='o', label=labels[w])


plt.xticks(kk_print)

plt.legend()
plt.xlabel("Bitlength of exponents")
plt.ylabel("Percentage gain")
plt.title("Verification computation time between naive multiexponentiation\n and Lenstra implementation with λ=" +
          str(lamda) + " using C interface")
plt.savefig(str(lamda) + "_C_time.pdf")
plt.show()


for w in ww:
    verif_time = []
    for i, k in enumerate(kk_values):
        file = open("result/" + str(t) + "_" + str(lamda) +
                    "_" + str(k) + "_" + str(w) + ".csv")

        temp_array = []

        for line in file:
            line_array = line.split(";")
            temp_array.append(float(line_array[3]))

        verif_time.append(100 - 100 * np.mean(temp_array) / naive_time[i])

    plt.plot(kk_print, verif_time, marker='o', label=labels[w])

plt.plot(kk_print, zero, label="Naive")
plt.xticks(kk_print)

plt.legend()
plt.xlabel("Bitlength of exponents")
plt.ylabel("Percentage gain")
plt.title("Percetagne of time acceleration between naive multiexponentiation\n and Lenstra implementation with λ=" +
          str(lamda) + " using C interface")
plt.savefig(str(lamda) + "_C_percentage.png")
plt.show()

#print("Naive implementation mean computation time : ", nm)
#print("Optimized implementation mean computation time : ", om)
#print("Percentage gain : ", 100 - (om / nm * 100))
