
lista_strings = []

lista_longitudes = []

longitud_actual = 0

string_actual = ""

while string_actual != "FIN":
    string_actual = input("Introduce una nueva string a la lista: ")
    if string_actual == "FIN":
        break

    lista_strings.append(string_actual)

    longitud_actual = len(string_actual)

    lista_longitudes.append(longitud_actual)

print("Las longitudes de las strings introducidas son, en orden: {}".format(lista_longitudes))
