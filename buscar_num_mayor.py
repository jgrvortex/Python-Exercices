
lista_numeros = [22,3,4,14,5,6,456,76,8,9,190,88,790,11,124,3,254,22,540,913,63,47,7,77,797,354,1008,9]

numero_mayor = 0

for numero_actual in lista_numeros:
    if numero_actual > numero_mayor:
        numero_mayor = numero_actual

print("La lista de numeros es: {}".format(lista_numeros))
print("El numero mayor de la lista es: {}".format(numero_mayor))
