
#Crear un programa que guarde e imprima varias listas con todos los números que estén dentro de una lista proporcionada por el usuario y sean múltiplos de 2, de 3, de 5 y de 7.

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,20,25,30,32,34,35,38,41,45,48,50,55,56,58,59,60,62,65,66,68,70,75,77,80,85,90,98,100,120]

multiplos_dos = []
multiplos_tres = []
multiplos_cinco = []
multiplos_siete = []

long = len(numeros)

indice_dos = 0
indice_tres = 0
indice_cinco = 0
indice_siete = 0

for indice in range(long):
    if numeros[indice] % 2 == 0:
        multiplos_dos.append(numeros[indice])
    elif numeros[indice] % 3 == 0:
        multiplos_tres.append(numeros[indice])
    elif numeros[indice] % 5 == 0:
        multiplos_cinco.append(numeros[indice])
    elif numeros[indice] % 7 == 0:
        multiplos_siete.append(numeros[indice])


print("Multiplos de 2: {}".format(multiplos_dos))
print("Multiplos de 3: {}".format(multiplos_tres))
print("Multiplos de 5: {}".format(multiplos_cinco))
print("Multiplos de 7: {}".format(multiplos_siete))