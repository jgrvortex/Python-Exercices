numero=int(input("Elige un numero: "))

if (numero<100 and numero>10) and numero%2==0:
    print("El numero introducido es par y esta dentro del intervalo permitido")
elif (numero<100 and numero>10) and numero%2!=0:
    print("El numero introducido es impar y esta dentro del intervalo permitodo")
else:
    print("El numero esta fuera del intervalo permitido")

while numero>0:
    print("El numero actual es: {}".format(numero))
    divs=int(numero/2+1)
    while divs>1:
        no_primo=(numero%divs==0)
        if noprimo==True:
            break
        divs -= 1

    if no_primo==True:
        print("Se trata de un numero no primo")
    else:
        print("Se trata de un numero primo")
    numero -= 1
