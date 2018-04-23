
lista_numeros = []

numero_actual = 0

multiplicacion_numeros = 1

while numero_actual != "FIN":
    numero_actual = input("Introduce un nuevo numero a la lista: ")
    if numero_actual == "FIN":
        break

    numero_actual = int(numero_actual)

    multiplicacion_numeros *= numero_actual

    lista_numeros.append(numero_actual)

print("La multiplicacion de los elementos de la lista {} es {}".format(lista_numeros,multiplicacion_numeros))