
frase_usuario = input("Introduce fragmento de texto para contar sus puntos, comas y espacios: ")

coma = ","
punto = "."
espacio = " "

numero_comas = 0
numero_puntos = 0
numero_espacios = 0


for letra in frase_usuario:
    if letra == coma:
        numero_comas += 1
    elif letra == punto:
        numero_puntos += 1
    elif letra == espacio:
        numero_espacios += 1

print("Numero de puntos: {}".format(numero_puntos))
print("Numero de comas: {}".format(numero_comas))
print("Numero de espacios: {}".format(numero_espacios))

