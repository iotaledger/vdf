import matplotlib.pyplot as plt
import numpy as np
import seaborn
from scipy.optimize import curve_fit

# ASIC
s9SE = [269, 1280, 16 * (10**12), 0]
s19 = [2789, 3250, 95 * (10**12), 0]
t17 = [1239, 3150, 58 * (10**12), 0]
s17_plus = [1889, 2920, 70 * (10**12), 0]
Innosilicon_T3_plus = [1987, 3300, 57 * (10**12), 0]
AvalonMiner1166 = [2267, 3196, 68 * (10**12), 0]
asics = [s9SE, s19, t17, s17_plus, Innosilicon_T3_plus, AvalonMiner1166]


# CLOUD
Cloud = [0, 0, 1 * (10**12), 89.90]


# GPU
AMD_Radeon_VII = [646, 300, 90 * (10**6), 0]
GeForceGTX1070 = [335, 150, 30 * 90 * (10**6), 0]
AMD_Radeon_RX580 = [130, 185, 2990 * (10**6), 0]
NvidiaGTX1080Ti = [1099, 250, 3290 * (10**6), 0]
AMD5870x6 = [90, 1150, 2568 * (10**6), 0]
gpus = [AMD_Radeon_VII, GeForceGTX1070,
        AMD_Radeon_RX580, NvidiaGTX1080Ti, AMD5870x6]


# FPGA
Bitcoin_Dominator_X5000 = [440, 6.8, 100 * (10**6), 0]
Butterflylabs_Mini_Rig = [15295, 1250, 25150 * (10**6), 0]
Icarus = [569, 19.2, 380 * (10**6), 0]
Lancelot = [350, 26, 400 * (10**6), 0]
X6500_FPGA_Miner = [550, 17.2, 400 * (10**6), 0]
ModMiner_Quad = [1069, 40, 800 * (10**6), 0]
BitForce_SHA256_Single = [599, 80, 832 * (10**6), 0]
fpgas = [Bitcoin_Dominator_X5000, Butterflylabs_Mini_Rig, Icarus,
         Lancelot, X6500_FPGA_Miner, ModMiner_Quad, BitForce_SHA256_Single, ]


# CPU
Core_i7_2600K = [60, 95, 18.6 * (10**6), 0]
Xeon_E7520_dual = [150, 95, 18 * (10**6), 0]
Core_i5_2400 = [20, 95, 14 * (10**6), 0]
Xeon_X5355_dual = [15, 120, 22.76 * (10**6), 0]
Xeon_Prestonia_2_4_dual = [20, 130, 2.17 * (10**6), 0]
Core_i7_980x = [82, 130, 19.2 * (10**6), 0]
Core_i7_620M = [25, 35, 6.2 * (10**6), 0]
Core_i3_530 = [10, 80,  8.31 * (10**6), 0]
cpus = [Core_i7_2600K, Xeon_E7520_dual,
        Core_i5_2400, Xeon_X5355_dual, Core_i7_980x, Xeon_Prestonia_2_4_dual, Core_i7_620M, Core_i3_530]

# IOT
RaspberryB = [10, 3.75, 0.2 * (10**6), 0]
Cortex_A8 = [70, 0.35, 0.125 * (10**6), 0]
Cortex_A9 = [70, 0.5, 0.57 * (10**6), 0]
AllWinner_A10 = [170, 2.5, 0.568 * (10**6), 0]
Marvel_Feroceon = [None, 0.87, 0.195 * (10**6), 0]
iots = [RaspberryB, Cortex_A8, Cortex_A9, AllWinner_A10]


vdf_f1 = [0, 0, 3 * 10 ** 7, 0.7]
vdf_fpga = [vdf_f1]


vdf_i7_7820HQ = [346, 45, 871350.3164388661, 0]
vdf_cpu = [vdf_i7_7820HQ]

vdf_raspberry_pi_3 = [45, 3.75, 6 * 10**4, 0]
vdf_iot = [vdf_raspberry_pi_3]


min_pow = 0.125 * (10**6)
min_vdf = 6 * 10**4


duration = 24 * 365 * 1
electricity_price = 0.076 / 1000  # France


def plot_hardware(hardware, label, min_value, color, s=500, marker=".", type="PoW", pool=False):

    linewidth = 1
    edgecolor = 'white'
    if pool_bool == True:
        edgecolor = color
        color = 'white'
        linewidth = 2
        s = 400
    min_y = 0
    min_x = 0

    for device in hardware:
        x = device[0] / duration + device[1] * electricity_price + device[3]
        x = 1.1 * x
        y = device[2] / min_value

        if y > min_y:
            min_y = y
            min_x = x

        if pool == True:
            x = x * 1000
            if type == 'PoW':
                y = y * 1000
        plt.scatter(x, y, s=s, marker=marker, color=color,
                    zorder=3, edgecolors=edgecolor, linewidth=linewidth)

    xx = np.linspace(min_x, 10, 10)
    if type == "VDF":
        yy = [min_y] * 10
    else:
        yy = xx * min_y / min_x
        print(label)
        print(min_y / min_x)
        print(yy)
        print()
    #plt.plot(xx, yy, color=color, linewidth=3)


pool_bool = False

plot_hardware(asics, 'ASIC', min_pow, 'red', type='PoW', pool=pool_bool)
plot_hardware(gpus, 'GPU', min_pow, 'blue', type='PoW', pool=pool_bool)
plot_hardware(fpgas, 'FPGA', min_pow, 'green', type='PoW', pool=pool_bool)
plot_hardware(cpus, 'CPU', min_pow, 'brown', type='PoW', pool=pool_bool)
plot_hardware(iots, 'IoT', min_pow, 'purple', type='PoW', pool=pool_bool)

plot_hardware(vdf_iot, 'IoT VDF', min_vdf, 'purple',
              s=500, marker="s", type="VDF", pool=pool_bool)
plot_hardware(vdf_cpu, 'CPU VDF', min_vdf, 'brown',
              s=500, marker="s", type="VDF", pool=pool_bool)
plot_hardware(vdf_fpga, 'FPGA VDF', min_vdf,
              'green', s=500, marker="s", type="VDF", pool=pool_bool)


pool_bool = True

plot_hardware(asics, 'ASIC', min_pow, 'red', type='PoW', pool=pool_bool)
plot_hardware(gpus, 'GPU', min_pow, 'blue', type='PoW', pool=pool_bool)
plot_hardware(fpgas, 'FPGA', min_pow, 'green', type='PoW', pool=pool_bool)
plot_hardware(cpus, 'CPU', min_pow, 'brown', type='PoW', pool=pool_bool)
plot_hardware(iots, 'IoT', min_pow, 'purple', type='PoW', pool=pool_bool)

plot_hardware(vdf_iot, 'IoT VDF', min_vdf, 'purple',
              s=500, marker="s", type="VDF", pool=pool_bool)
plot_hardware(vdf_cpu, 'CPU VDF', min_vdf, 'brown',
              s=500, marker="s", type="VDF", pool=pool_bool)
plot_hardware(vdf_fpga, 'FPGA VDF', min_vdf,
              'green', s=500, marker="s", type="VDF", pool=pool_bool)

plt.scatter([], [], color='red', label='ASIC', s=150)
plt.scatter([], [], color='blue', label='GPU', s=150)
plt.scatter([], [], color='green', label='FPGA', s=150)
plt.scatter([], [], color='brown', label='CPU', s=150)
plt.scatter([], [], color='purple', label='IoT', s=150)

plt.scatter([], [], color='black', label='PoW x1', s=150)
plt.scatter([], [], color='black', marker='s', label='VDF x1', s=150)


plt.scatter([], [], color='white', label='PoW x1000',
            s=100, linewidth=2, edgecolors='black')
plt.scatter([], [], color='white', marker='s', label='VDF x1000',
            s=100, linewidth=2, edgecolors='black')

'''
gpus_cost = [x[0] / duration + x[1] * electricity_price for x in gpus]
gpus_hashrate = [x[2] for x in gpus]

gpus_coef = np.polyfit(gpus_cost, gpus_hashrate, 1)
gpus_poly1d_fn = np.poly1d(gpus_coef)
plt.plot(gpus_cost, gpus_hashrate, 'bo',
         gpus_cost, gpus_poly1d_fn(gpus_cost), '--k')
'''

plt.legend()
plt.ylabel("Speedup in thoughput")
plt.xlabel("Price in USD per hour")

plt.yscale("log")
plt.xscale('log')

plt.grid()
plt.grid(b=True, which='minor', color='lightgrey',
         linestyle='-', axis='both')
plt.grid(b=True, which='major', color='grey',
         linestyle='-', axis='both')
plt.rc('axes', axisbelow=True)

suffix = ''
if pool_bool:
    suffix = "_pool"
plt.savefig("hardware_price" + suffix + ".pdf", bbox_inches='tight')
plt.show()
