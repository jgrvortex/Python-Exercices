
frase_usuario = input("Escribe una frase para que el programa visualice todas sus vocales: ")

vocales = ["a","e","i","o","u","A","E","I","O","U"]

vocales_presentes = []

posicion = 0

for letra in frase_usuario:
    if letra in vocales:
        vocales_presentes.append(letra)

print(vocales_presentes)