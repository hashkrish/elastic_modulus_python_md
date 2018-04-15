import matplotlib.pyplot as plt
import csv
import numpy as np

strainX = []
stressX = []
stressY = []
stressZ = []

time = []
lx = []
ly = []
lz = []
vol = []
press = []
pe = []
ke = []
etotal = []
temp = []

with open('/home/krish/elastic_modulus_python_md/lammps_files/report/Al_SC_100.def1.txt','r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=' ')
	next(csv_reader)
	i=0
	for line in csv_reader:
		strainX.append(line[0])
		stressX.append(line[1])
		stressY.append(line[2])
		stressZ.append(line[3])

with open('/home/krish/elastic_modulus_python_md/lammps_files/report/Al_SC_100.eq1.txt','r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=' ')
	next(csv_reader)
	i=0
	for line in csv_reader:
		time.append(line[0])
		lx.append(line[1])
		ly.append(line[2])
		lz.append(line[3])
		vol.append(line[4])
		press.append(line[5])
		pe.append(line[6])
		ke.append(line[7])
		etotal.append(line[8])
		temp.append(line[9])

strainX = np.array(strainX).astype(np.float)
stressX = np.array(stressX).astype(np.float)
stressY = np.array(stressY).astype(np.float)
stressZ = np.array(stressZ).astype(np.float)

plt.rc('font', family='serif')

plt.plot(strainX, stressX, c='b')
plt.xlabel('Strain along X-Direction')
plt.ylabel('Stress in GPa')
plt.title('Stress-Strain Graph')
plt.savefig('stress-strain.jpg')
plt.show()

E = stressX/strainX
plt.scatter(range(E.size), E, c='b', s=1.5)
plt.xlabel('Timestep')
plt.ylabel('Youngs Modulus in GPa')
plt.title('Variation of Youngs Modulus with timestep')
plt.savefig('time-youngsModulus.jpg')
plt.show()
	
time = np.array(time).astype(np.float)
lx = np.array(lx).astype(np.float)
ly = np.array(ly).astype(np.float)
lz = np.array(lz).astype(np.float)
vol = np.array(vol).astype(np.float)
press = np.array(press).astype(np.float)
pe = np.array(pe).astype(np.float)
ke = np.array(ke).astype(np.float)
etotal = np.array(etotal).astype(np.float)
temp = np.array(temp).astype(np.float)

plt.plot(time, lx, 'b', time, ly, 'r', time, lz, 'g')
plt.xlabel('Timestep')
plt.ylabel('Length in Angstrom')
plt.title('Variation of Box Dimension with timestep')
plt.legend(['Length along x-axis','Length along y-axis','Length along z-axis'])
plt.savefig('time-boxdim.jpg')
plt.show()

plt.plot(time, vol, 'b')
plt.xlabel('Timestep')
plt.ylabel('Volume in Angstrom^3')
plt.title('Variation of Box Volume with timestep')
plt.savefig('time-boxvol.jpg')
plt.show()

plt.plot(time, press, 'b')
plt.xlabel('Timestep')
plt.ylabel('Pressure in GPa')
plt.title('Variation of Box Pressure with timestep')
plt.savefig('time-pressure.jpg')
plt.show()

plt.plot(time, press, 'b')
plt.xlabel('Timestep')
plt.ylabel('Pressure in GPa')
plt.title('Variation of Pressure with timestep')
plt.savefig('time-pressure.jpg')
plt.show()

plt.plot(time, pe, 'b', time, ke, 'r', time, etotal, 'g')
plt.xlabel('Timestep')
plt.ylabel('Length in Angstrom')
plt.title('Variation of Energy with timestep')
plt.legend(['Potential Energy in eV','Total Energy in eV','Total Energy in eV'])
plt.savefig('time-energy.jpg')
plt.show()

plt.plot(time, temp, 'b')
plt.xlabel('Timestep')
plt.ylabel('Temperature in Kelvin')
plt.title('Variation of Temperature with timestep')
plt.savefig('time-temperature.jpg')
plt.show()
