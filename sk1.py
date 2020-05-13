import matplotlib.pyplot as plt
import numpy as np

with open('energy.txt', 'r') as file:
    energy = file.read()

with open('time.txt', 'r') as file:
    time = file.read()

energy = energy.split(' ')
energy = [float(p) for p in energy if p and p[0] == '-']
time = time.split(' ')
time = [float(p.strip()) for p in time if p and p != '\n']

fig, ax = plt.subplots()
ax.plot(time, np.asarray(energy, np.float32), 'r-+')
ax.set_xlabel('PWSCF[s]')
ax.set_ylabel('energia całkowita [Ry]')
ax.set_title('Zależność Energii całkowitej układu od czasu')
fig.savefig('skrypt3')

print(time)
print(energy)
