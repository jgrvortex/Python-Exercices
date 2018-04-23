
lista_numeros = []

indice_actual = 0

numero_mas_pequeño = 0

numero = 0

while numero != "FIN":

    numero = input("Introduce un numero para incorporarlo en la lista: ")
    if numero == "FIN":
        break
    numero = int(numero)

    if indice_actual == 0:
        numero_mas_pequeño = numero

    lista_numeros.append(numero)

    if numero < numero_mas_pequeño:
        numero_mas_pequeño = numero

    indice_actual += 1


longitud = len(lista_numeros)

print("La lista de numeros introducida es: {}".format(lista_numeros))
print("El numero mas pequeño de la lista es {}".format(numero_mas_pequeño))

