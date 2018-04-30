
#Realizar el FizzBuzz con las mismas reglas pero en el caso que el numero sea divisible entre 3 y 5, cambiar el texto por “Bazinga”.

numeros = [1,2,3,4,6,8,9,11,15,23,1,115,16,17,18,24,25,26,27,28,41,42,43,44,45,46,50,60,70,100]

long = len(numeros)

for indice in range(long):

    #Aquí utilizo otra forma distinta de estructurar las distintas opciones y condiciones de las que aparecen en el vídeo

    if numeros[indice] % 3 == 0 and numeros[indice] % 5 != 0:
        numeros[indice] = "Fizz"
    elif numeros[indice] % 5 == 0 and numeros[indice] % 3 != 0:
        numeros[indice] = "Buzz"
    elif numeros[indice] % 3 == 0 and numeros[indice] % 5 == 0:
        numeros[indice] = "Bazinga"

print(numeros)