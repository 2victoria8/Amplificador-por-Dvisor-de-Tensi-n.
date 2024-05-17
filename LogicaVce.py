vcc= int(input("colocar el valor de vcc:"))
beta=int(input("colocar el valor del beta:"))
R1= int(input("por favor colocar valor de R1:"))
R2= int (input("por favor colocar valor de R2:"))
Re= int (input("por favor colocar valor de Re:"))
Rc= int (input("por favor colocar valor de Rc:"))
Ib=("x")
Ic=Ib*beta

def genIb(R1, R2, vcc, beta, Re):
    multiplicación=R1*R2
    suma=R1+R2
    paralelo=multiplicación/suma

    multiplicación=vcc*R2
    suma=R1+R2
    Voltaje_de_Thevenin=multiplicación/suma

    vbe=0.7
    resta=Voltaje_de_Thevenin - vbe

    divisor=beta+1
    divisor2=divisor*Re
    divisor3=divisor2+divisor
    Ib=resta/divisor3
    return Ib
def genIc(R1, R2, vcc, beta, Re):
    Ib = genIb(R1, R2, vcc, beta, Re)
    Ic=Ib*beta
    return Ic
Ic = genIc(R1, R2, vcc, beta, Re)
Vc=vcc-Ic*Rc
vbe=0.7
multiplicación=vcc*R2
suma=R1+R2
Vb=multiplicación/suma
Ve=Vb-vbe
Vce=Vc-Ve
print("Vce= ",Vce,"V")