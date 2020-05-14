import matplotlib.pyplot as plt
import subprocess

tau = [i for i in range(10, 28)]
values = []

for i in tau:
    result = subprocess.run(
        ['src/bin/vdf', str(i), '2048', '128', '2'], stdout=subprocess.PIPE)
    print(float(result.stdout))
    print(float(result.stdout) / (2**i))
    print()
    values.append(1000000 * float(result.stdout) / (2**i))

plt.plot(tau, values)
plt.show()
