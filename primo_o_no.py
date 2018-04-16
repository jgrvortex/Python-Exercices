#Este es un ejercicio de práctica que he hecho por mi cuenta para practicar un poco
#Es el típico ejercicio de verificar si el número introducido es primo o no pero con variaciones
#En este caso primo se verifica si el número es par o no y si está dentro del intervalo establecido
#Luego se calculan todos los números más pequeños que éste y el programa averigua, para cada uno de ellos, si es primo o no

numero = int(input("Elige un numero: "))

if (numero < 100 and numero > 10) and numero % 2 == 0:
    print("El numero introducido es par y esta dentro del intervalo permitido")
elif (numero < 100 and numero > 10) and numero % 2 != 0:
    print("El numero introducido es impar y esta dentro del intervalo permitodo")
else:
    print("El numero esta fuera del intervalo permitido")

while numero > 0:
    print("El numero actual es: {}".format(numero))
    divs = int(numero / 2 + 1)
    while divs > 1:
        no_primo = (numero % divs == 0)
        if no_primo == True:
            break
        divs -= 1

    if no_primo == True:
        print("Se trata de un numero no primo")
    else:
        print("Se trata de un numero primo")
    numero -= 1
