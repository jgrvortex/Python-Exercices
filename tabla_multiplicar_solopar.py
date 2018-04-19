
numero = int(input("De que numero quieres la tabla de multiplicar? "))

for num in range(1,11):
    if num % 2 == 0:
        resultado = numero * num
        print("{} x {} = {}".format(numero,num,resultado))