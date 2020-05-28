import matplotlib.pyplot as plt
import numpy as np

t_values = range(10, 15)
lambda_values = ['4096', '2048', '1024']
lambda_markers = {'1024': 'o', '2048': 's', "4096": "d"}
k = 128
w = 0


lambda_color = {'1024': 'green', '2048': 'blue', "4096": "red"}

plt.plot([], [], color="black", ls="--", label="IoT")
plt.plot([], [], color="black", ls="-", label="CPU")


for lamda in lambda_values:
    display_value = []
    for t in t_values:
        f = open("result/" + str(t) + "_" + str(lamda) +
                 "_" + str(k) + "_" + str(w) + ".csv")
        verif_time = []

        for line in f:
            verif_time.append(1000 * float(line.split(';')[3]))
        display_value.append(np.min(verif_time))

    plt.plot(t_values, display_value,
             color=lambda_color[lamda], label="$\lambda$=" + lamda, marker=lambda_markers[lamda])


for lamda in lambda_values:
    display_value = []
    for t in t_values:
        f = open("result_rp/" + str(t) + "_" + str(lamda) +
                 "_" + str(k) + "_" + str(w) + ".csv")
        verif_time = []

        for line in f:
            verif_time.append(1000 * float(line.split(';')[3]))
        display_value.append(np.min(verif_time))

    plt.plot(t_values, display_value, ls='dashed',
             color=lambda_color[lamda], marker=lambda_markers[lamda])


#plt.ylim([0, 0.0035])
plt.legend()
plt.yscale('log')
plt.grid(b=True, which='major', color='k', linestyle='-', axis='y')
plt.grid(b=True, which='minor', color='lightgrey', linestyle='-', axis='y')

plt.xlabel("Challenge - number of squarings")
plt.ylabel("Verification time (ms)")

plt.xticks([10, 11, 12, 13, 14], [
           '$2^{10}$', '$2^{11}$', '$2^{12}$', '$2^{13}$', '$2^{14}$'])

plt.savefig("log.pdf", bbox_inches='tight')
plt.show()
