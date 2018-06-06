
string_elegida = ""
palabra_actual = ""
lista_palabras = []
palabras_usadas = []
borrar_list = []
veces = dict()
borrar_dict = dict()

opcion = ""

while opcion != "N":
    opcion = input("Quieres contar el numero de veces que cada palabra de una string aparece en ella?: ")
    if opcion == "N" or opcion == "n":
        break
    if opcion == "S" or opcion == "s":
        string_elegida = input("Introduce la string: ")

    lista_palabras = string_elegida.split()

    long = len(lista_palabras)

    apariciones = 1
    numero = 1
    pos = 0
    for palabra in lista_palabras:
        pos += 1
        numero = pos
        if palabra in palabras_usadas:
            continue
        for num in range(numero,long):
            if palabra == lista_palabras[num]:
                apariciones += 1

        palabras_usadas.append(palabra)
        elemento = palabra
        apariciones = str(apariciones)
        veces[elemento] = apariciones
        apariciones = int(apariciones)
        apariciones = 1

    print("{}".format(veces))

    palabras_usadas = borrar_list
    veces = borrar_dict