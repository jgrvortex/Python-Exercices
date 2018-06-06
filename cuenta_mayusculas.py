
frase_usuario = input("Introduce una frase para contar las letras mayusculas: ")

mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

numero_mayusculas = 0

for letra in frase_usuario:
    if letra in mayusculas:
        numero_mayusculas += 1

print("El numero de letras mayusculas en la frase es: {}".format(numero_mayusculas))
