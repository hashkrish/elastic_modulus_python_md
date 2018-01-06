import math
element =raw_input("What element are you investigating? This will calcuate macro and microscopic Young's Modulus based on an example in Matter & Interactions 3rd Ed")
print element
print "mol=" ,6.02e23, "atoms"
ma = raw_input("What is the hanging mass in kilograms?")
print "ma=", ma,"kg"
ma=float(ma)
rho = raw_input("What is the density in kg/meters-cubed?")
print "rho=", rho, "kg/m^3"
rho=float(rho)
ama=raw_input("what is the atomic mass in kilograms?")
ama=float(ama)
print "ama=atomic mass", ama ,"kg"
mol =6.02e23
print
print "calculations"
vol=(ma/rho)
print "ma/rho=volume=",vol, "m^3"
print "total number atoms = N = rho*(mol/ama)", rho*(mol/ama)
N=rho*(mol/ama)
print "edge of 1m cube, number of atoms=", math.pow(N, 1/3) 
atoms= math.pow(N, 1/3) 
print
print "in one meter of atoms there are =", math.pow(N, 1/3), "atoms" 
diam=1/atoms
print "the diameter of one copper atom =", diam,"m"
print 
#print "one atom =", atoms/1, "meters"
print "Finding the spring constant of an interatomic bond"
print
print "data"
L =raw_input("how long is the wire in meters?")
L =float(L)
print "L=length of original wire", L, "m" #length of the wire originally
S=raw_input("what is the change in length in mm")
S=float(S)
print "S=change in length when weight is hung from the wire", S, "mm" #length of stretch
Sm=(S/1000)
print "S in meters", Sm, "m"
print
print "cacluations"
print "Ks= macro spring constant for wire=weight/distance"
M=10
print "M= mass placed on the wire =", M,"kg"
weight=M*9.8
print "weight =", M*9.8, "N"
print "Ks = Weight/change in length", (M*9.8)/S,"N/m"
Ks=(M*9.8)/S  
print "NL=Number of Atoms in one chain length", L/(1/atoms), "atoms"
NL=L/(1/atoms)
w=raw_input("width of the wire in millimeters?")
w =float(w)
d=raw_input("depth of the wire in millimeters?")
d = float(d)
print "w=width of rectangular wire=", (w/1000), "m"
wm=w/1000
print "d=depth of rectangular wire=", (d/1000), "m"
dm=d/1000
A=wm*dm
print "A = area of the wire", A, "m^2"
Aa=diam*diam
print "Aa = area of an atom", Aa, "m^2"
NA=(A/Aa)
print "NA=Number of atoms in a cross-sectional area of wire",NA,"atoms"
print "Km= interatomic spring constant for copper"
print "Ks=((Km*NA)/NL)"
Km=(Ks*NL)/NA
print "Km =((Ks*NL)/NA)",Km ,"N/m"
YMmac=((weight/A)*(L/S))
print "Young's Modulus: Macroscopic = (Force tension*wire length)/(wire area*change in length due to wieght", YMmac, "Pa"
YMmicro=Km/diam
print "YMmicro=Microscopic Spring Constant/atomic diameter"
print "Young's Modulus:Microscopic", YMmicro, "Pa"