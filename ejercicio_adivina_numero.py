
numero_correcto = 71


print("Intenta adivinar el numero escondido, comprendido en el intervalo del 1 al 99, incluidos ambos.")

numero_elegido = 0
while numero_elegido != numero_correcto:

    intervalo = False
    while intervalo == False:
        numero_elegido = int(input("Introduce un numero: "))
        intervalo = (numero_elegido > 0 and numero_elegido < 100)
        if intervalo == False:
            print("El numero debe de ser mayor que 0 y menor que 100. Gracias...")
    if numero_elegido == numero_correcto:
        print("Fabuloso!! Has acertado el numero!!")
    else:
        print("El numero introducido no es correcto. Quiza el futuro aspirante consiga acertar...")