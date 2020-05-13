import matplotlib.pyplot as plt
import numpy

with open('energy.txt', 'r') as file:
    energy = file.read()

with open('time.txt', 'r') as file:
    time = file.read()

energy = energy.split(' ')
energy = [float(p) for p in energy if p and p[0] == '-']
time = time.split(' ')
time = [float(p.strip()) for p in time if p and p != '\n']

fig,ax = plt.subplots()
ax.plot(time, energy, 'r-+')
ax.set(xlabel='PWSCF[s]', ylabel='energia całkowita [Ry]', title='Zależność energii całkowitej osiągniętej przez układ od czasu obliczeń')
ax.grid()
fig.savefig('skrypt1')

print(time)
print(energy)
