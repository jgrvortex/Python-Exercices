
lista_elementos = []

numero_actual = 0

suma_elementos = 0

indice_actual = 0

while numero_actual != "FIN":
    numero_actual = input("Introduce un nuevo numero a la lista para despues calcular la media total: ")
    if numero_actual == "FIN":
        break
    else:
        numero_actual = int(numero_actual)
        lista_elementos.append(numero_actual)
        indice_actual += 1
        suma_elementos += numero_actual

media = suma_elementos / indice_actual

print("La media de los numeros introducidos en la lista es: {}".format(media))
