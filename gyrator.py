import math

F = [700,1000,1500,2300,3500,5600]
Q = [1.6,1.6,1.6,1.7,1.7,1.6]
R = 1000

#calculate ideal capacitor values for equal-R gyrator
for x in range(0,6,1):
    C1 = 1/(4*math.pi*R*Q[x]*F[x])
    C2 = Q[x]/(math.pi*R*F[x])
    print(F[x],"Hz:",round(C1*1e+9,1),"nF,",round(C2*1e+9,1),"nF,")

print("######")

#calculate variance from target frequency
C1 = [68e-9,47e-9,33e-9,20e-9,13.3e-9,9e-9]
C2 = [727e-9,517e-9,330e-9,235e-9,150e-9,90e-9]
for x in range(0,6,1):
    F2 = 1/(2*math.pi*R*math.sqrt(C1[x]*C2[x]))
    print(round(F2,0),"Hz, Variance =",round((F2-F[x])/F[x],3),"%")
