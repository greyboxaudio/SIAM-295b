import numpy as np

RE = 1500
F = [700,1000,1500,2300,3500,5600]
Q = 1.7
R1 = 1000
R2 = 100000

db = 20*np.log10((RE+R1)/R1)
print(db)

for x in F:
    C1 = 1/(2*np.pi*x*R1*Q)
    L = 1/(np.square((2*np.pi*x))*C1)
    C2 = L/(R1*R2)
    print(x,"Hz")
    print(np.round((C1*1000000000),1),"nF")
    print(np.round(L,3),"H")
    print(np.round((C2*1000000000),3),"nF"),

print("######")
#Ideal Capacitance
#0.7 kHz = 134n / 3n9
#1.0 kHz = 94n / 2n7
#1.5 kHz = 62n / 1n8
#2.3 kHz = 41n / 1n2
#3.5 kHz = 27n / 770p
#5.6 kHz = 17n / 480p

#calculate R2 for standard capacitor values
C1x = [133e-09,100e-09,68e-09,43e-09,25e-09,15e-09]
C2x = [3.3e-09,2.2e-09,1.5e-09,1e-09,0.68e-09,0.47e-09]
for i in range(0,6,1):
    C1 = C1x[i]
    L = 1/(np.square((2*np.pi*F[i]))*C1)
    C2 = C2x[i]
    R2x=L/R1/C2
    print(F[i],"Hz")
    print(np.round((R2x/1000),1),"kOhms")