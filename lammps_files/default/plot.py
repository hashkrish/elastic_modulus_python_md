import matplotlib.pyplot as plt
import csv
import numpy as np

strainX = []
stressX = []
stressY = []
stressZ = []

with open('/home/krish/elastic_modulus_python_md/lammps_files/default/Al_SC_100.def1.txt','r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=' ')
	next(csv_reader)
	i=0
	for line in csv_reader:
		strainX.append(line[0])
		stressX.append(line[1])
		stressY.append(line[2])
		stressZ.append(line[3])

strainX = np.array(strainX).astype(np.float)
stressX = np.array(stressX).astype(np.float)
stressY = np.array(stressY).astype(np.float)
stressZ = np.array(stressZ).astype(np.float)

plt.plot(strainX, stressX)
plt.show()

E = stressX/strainX

plt.plot(range(E.size), E)
plt.show()
	


