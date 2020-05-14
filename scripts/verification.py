import matplotlib.pyplot as plt
import numpy as np

t_values = range(20, 25)
lambda_values = ['1024', '2048', '4096']
k = 256
w = 0

for lamda in lambda_values:
    display_value = []
    for t in t_values:
        f = open("result/" + str(t) + "_" + str(lamda) +
                 "_" + str(k) + "_" + str(w) + ".csv")
        verif_time = []

        for line in f:
            verif_time.append(float(line.split(';')[3]))
        display_value.append(np.max(verif_time))

    plt.plot(t_values, display_value)
#plt.ylim([0, 0.0035])
plt.yscale("log")
plt.show()
