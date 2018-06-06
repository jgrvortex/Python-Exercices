
enteros = ["0","1","2","3","4","5","6","7","8","9"]

lista_general = []

lista_enteros = []

lista_strings = []

lista_elementos_mixtos = []
#Esta lista es necesaria para el caso en que el elemento introducido contenga números y letras simultáneamente

elemento_actual = ""

indice_actual = 0

while elemento_actual != "FIN":
    elemento_actual = input("Introduce un nuevo elemento para clasificarlo como entero o como cadena de caracteres: ")
    if elemento_actual == "FIN":
        break

    caracterentero = 0

    caracterstring = 0

    long = len(elemento_actual)

    for indice_actual in range(long):
        if elemento_actual[indice_actual] in enteros:
            caracterentero += 1
        else:
            caracterstring += 1

    if caracterentero > 0 and caracterstring == 0:
        lista_enteros.append(elemento_actual)
    elif caracterentero == 0 and caracterstring > 0:
        lista_strings.append(elemento_actual)
    else:
        lista_elementos_mixtos.append(elemento_actual)

print("Los enteros introducidos son los siguientes: {}".format(lista_enteros))
print("Las strings introducidas son las siguientes: {}".format(lista_strings))
print("Los elementos que contienen numeros y letras son los siguientes: {}".format(lista_elementos_mixtos))



