R1= int(input("por favor colocar valor de R1:"))
R2= int (input("por favor colocar valor de R2:"))
Re= int (input("por favor colocar valor de Re:"))

vcc= int(input("colocar el valor de vcc:"))
multiplicación=vcc*R2
suma=R1+R2
Vb=multiplicación/suma

Vbe=0.7

Ve=Vb-Vbe
print("Ve= ",Ve, "V")