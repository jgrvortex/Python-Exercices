
frase_usuario = input("Escribe una frase para que el programa cuente el numero de vocales y de consonantes: ")

vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

numeros = [1,2,3,4,5,6,7,8,9,0]

espacio = " "

longitud = len(frase_usuario)

num_vocales = 0
num_espacios = 0
num_consonantes = 0
num_numeros = 0

for letra in frase_usuario:
    if letra in vocales:
        num_vocales += 1
    elif letra == espacio:
        num_espacios += 1
    elif letra in numeros:
        num_numeros += 1
    else:
        num_consonantes += 1

suma = num_vocales + num_consonantes + num_numeros + num_espacios

print("El numero de vocales en la frase es de: {}".format(num_vocales))
print("El numero de consonantes en la frase es de: {}".format(num_consonantes))
print("El numero de espacios en la frase es de: {}".format(num_espacios))
print("El numero total de caracteres en la frase es de: {}".format(longitud))
print("La suma de los numeros, vocales, consonantes y espacios contados es: {}".format(suma))