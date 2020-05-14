import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['IoT', 'CPU', 'FPGA', 'ASIC']
pow_l = [2 * (10**5), 6 * (10**7), 3 * (10**10), 2 * (10**13)]
vdf_l = [3 * (10**4), 10**6, 3 * (10**7), 0]
vdf_l_h = [3 * (10**4), 0, 0, 10**9]

pow_l = [x / pow_l[0] for x in pow_l]
vdf_l = [x / vdf_l[0] for x in vdf_l]
vdf_l_h = [x / vdf_l_h[0] for x in vdf_l_h]


x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
minor_ticks = np.arange(0, 1, 1)

sided = 1
if sided:
    rects2 = ax.bar(x - width / 2, vdf_l_h, width,
                    color="lightgreen", zorder=3)
    rects2 = ax.bar(x - width / 2, vdf_l, width,
                    label='VDF', color="green", zorder=3)
    rects1 = ax.bar(x + width / 2, pow_l, width,
                    label='PoW', color="red", zorder=3)
else:
    rects1 = ax.bar(x, pow_l, width, label='PoW', color="red")
    rects2 = ax.bar(x, vdf_l_h, width, label='VDF', color="green", hatch="//")
    rects3 = ax.bar(x, vdf_l, width, label='VDF', color="green")


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Multiplication factor')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.yscale("log")
fig.tight_layout()

plt.grid(b=True, which='major', color='k', linestyle='-', axis='y')
plt.grid(b=True, which='minor', color='k', linestyle='-', axis='y')
ax.minorticks_on()

ax.yaxis.set_minor_locator(AutoMinorLocator(4))


plt.savefig("stacked.pdf")
plt.show()


labels = ['IoT', 'CPU', 'FPGA']


R_pow = [2 * (10**5), 66 * (10 ** 6), 25 * (10**9)]
P_pow = [3.75, 130, 1250]
E_pow = [x / y for x, y in zip(R_pow, P_pow)]
E_pow = [x / E_pow[0] for x in E_pow]

R_vdf = [3 * (10**4), 10**6, 3 * (10**7)]
P_vdf = [3.75, 45, 50]
E_vdf = [x / y for x, y in zip(R_vdf, P_vdf)]
E_vdf = [x / E_vdf[0] for x in E_vdf]


x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
minor_ticks = np.arange(0, 1, 1)

sided = 1
if sided:
    rects2 = ax.bar(x - width / 2, E_vdf, width,
                    label='VDF', color="green", zorder=3)
    rects1 = ax.bar(x + width / 2, E_pow, width,
                    label='PoW', color="red", zorder=3)
else:
    rects1 = ax.bar(x, pow_l, width, label='PoW', color="red")
    rects2 = ax.bar(x, vdf_l_h, width, label='VDF', color="green", hatch="//")
    rects3 = ax.bar(x, vdf_l, width, label='VDF', color="green")


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Multiplication factor')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.yscale("log")
fig.tight_layout()

plt.grid(b=True, which='major', color='k', linestyle='-', axis='y')
plt.grid(b=True, which='minor', color='k', linestyle='-', axis='y')
plt.minorticks_on()

plt.savefig("stacked.pdf")
plt.show()
