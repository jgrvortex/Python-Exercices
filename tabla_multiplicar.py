
numero = int(input("De que numero quieres la tabla de multiplicar? "))

for num in range(5,16):
    resultado = numero * num
    print("{} x {} = {}".format(numero,num,resultado))