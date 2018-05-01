
tres_numeros = [11, 63, 65]

def encuentra_mayor_numero(lista):
    mayor = lista[0]
    if lista[1] > mayor:
        mayor = lista[1]
    if lista[2] > mayor:
        mayor = lista[2]
    return mayor

numero_mayor = encuentra_mayor_numero(tres_numeros)

print("El numero mayor de la lista {} es: {}".format(tres_numeros, numero_mayor))