import matplotlib.pyplot as plt
import subprocess

tau = [i for i in range(10, 28)]
values = []

k = '2048'

print("K = " + k)

for i in tau:
    result = subprocess.run(
        ['src/bin/vdf', str(i), k, '128', '2'], stdout=subprocess.PIPE)
    print("Tau = 2**" + str(i))
    print("Time spent on eval : " + str(float(result.stdout)))
    print("Squares per second : " + str(2**i / float(result.stdout)))
    print()
    values.append(1000000 * float(result.stdout) / (2**i))

plt.plot(tau, values)
plt.show()
