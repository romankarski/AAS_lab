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

plt.figure()
plt.plot(time, energy, 'r-+')
plt.xlabel('PWSCF[s]')
plt.ylabel('energia całkowita [Ry]')
plt.yscale('linear')
plt.title('Zależność Energii całkowitej układu od czasu')
plt.savefig('skrypt2')

print(time)
print(energy)
