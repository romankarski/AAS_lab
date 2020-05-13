import matplotlib.pyplot as plt
import numpy as np

with open('time_procek.txt', 'r') as file:
    time_procek = file.read()

time_procek = time_procek.split(' ')
time_procek = [float(p.strip()) for p in time_procek if p and p!= '\n']
time_procek = [time_procek[x] for x in [0,1,3,6]]

fig, ax = plt.subplots()
ax.bar([1,2,3,4], np.asarray(time_procek, np.float32))
ax.set_xlabel('Liczba procesorów')
ax.set_ylabel('PWCSF [s]')
ax.set_title('Zależność czasu obliczeń od liczby procesorów')
plt.subplots_adjust(wspace=0.2, hspace=0.2, left=0.2, bottom=0.1, right=0.9, top=0.8)
fig.savefig('skrypt2_plot')


print(time_procek)
