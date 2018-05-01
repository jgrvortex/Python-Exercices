
lista_numeros = [2,3,4,6,10,15,16,20,22,23,33,35,36,40,49,55,67,68]

def devuelve_pares(lista_numeros):
    lista_pares = []
    for numero in lista_numeros:
        if numero % 2 == 0:
            lista_pares.append(numero)

    return lista_pares

pares = devuelve_pares(lista_numeros)

print("Los numeros pares de la lista son los siguientes: {}".format(pares))