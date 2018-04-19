
lista_elementos = []

indice_actual = 0

elemento_actual = 0

while elemento_actual != "FIN":
    elemento_actual = input("Introduce un nuevo elemento a la lista: ")
    if elemento_actual == "FIN":
        break
    else:
        lista_elementos.append(elemento_actual)

    indice_actual += 1

largo_lista = indice_actual

print("El numero de elementos de la lista es: {}".format(largo_lista))
