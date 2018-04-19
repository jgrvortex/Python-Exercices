
numero = int(input("De que numero quieres la tabla de multiplicar invertida? "))

for num in range(1,11):
    resultado = numero * (11 - num)
    print("{} x {} = {}".format(numero,11 - num,resultado))