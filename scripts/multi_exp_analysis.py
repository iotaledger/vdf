import os
import numpy as np
import matplotlib.pyplot as plt

naive = []
opti = []

t = 8
kk = [1, 2, 3, 4, 5, 6, 7, 8]
kk_values = [2**k for k in kk]
kk_print = [2**(k + 1) for k in kk]
lamda = 2048
ww = [2, 3, 4]
zero = [0 for k in kk]

for w in ww:
    print(w)
    percentages = []
    for k in kk_values:
        print("\t" + str(k))
        for i in range(5):
            file = open("result/" + str(t) + "_" + str(lamda) +
                        "_" + str(k) + "_" + str(w) + ".csv")

            naive_array = []
            opti_array = []

            for line in file:
                line_array = line.split(";")
                naive_array.append(float(line_array[3]))
                opti_array.append(float(line_array[4]))

            naive.append(np.mean(naive_array))
            opti.append(np.mean(opti_array))

            nm = np.mean(naive)
            om = np.mean(opti)
        percentages.append(100 - (om / nm * 100))
    plt.plot(kk_print, percentages, marker='o', label="W=" + str(w))

plt.plot(kk_print, zero, color="black",
         marker='o', label="Naive implementation")
plt.xticks(kk_print)

plt.legend()
plt.xlabel("Bitlength of exponents")
plt.ylabel("Percentage gain")
plt.title("Percetagne of time acceleration between naive multiexponentiation and Lenstra implementation with λ=" + str(lamda))
plt.show()

#print("Naive implementation mean computation time : ", nm)
#print("Optimized implementation mean computation time : ", om)
#print("Percentage gain : ", 100 - (om / nm * 100))
