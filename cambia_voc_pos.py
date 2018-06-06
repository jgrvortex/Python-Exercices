
vocales = ["a","e","i","o","u","A","E","I","O","U"]

string_actual = []

while string_actual != "FIN":
    string_actual = input("Introduce una string para reemplazar sus vocales por su numero de aparicion: ")
    if string_actual == "FIN":
        break

    long = len(string_actual)

    num_sust = 1
    lista_string = list(string_actual)

    for indice_actual in range(long):

        if lista_string[indice_actual] in vocales:
            num_sust = str(num_sust)
            lista_string[indice_actual] = lista_string[indice_actual].replace(lista_string[indice_actual],num_sust)
            num_sust = int(num_sust) + 1

    lista_string = "".join(lista_string)
    print(lista_string)
    
