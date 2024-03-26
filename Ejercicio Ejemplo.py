salario=float(input("Ingrese su salario actual: "))
antiguo=int(input("Ingrese su antiguedad en la empresa: "))
if antiguo<3:
    bono=0
else:
    if antiguo<6:
        bono=0.10
    else:
        if antiguo<10:
            bono=0.15
        else:
            if antiguo<15:
                bono=0.20
            else:
                bono=0.50
total=salario+salario*bono
bonoT=bono*salario
print ("Tu salario actual es: ",salario)
print ("Tu bono por antiguedad es: ",bonoT)
print ("El total ganado es: ",total)

if bonoT>0:
    print ("Felicidades ganaste un bono adicional :D")
        

