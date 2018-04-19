operacion = input("¿Que operacion deseas realizar? (multiplicar, dividir, sumar, restar): ")

primer_numero = int(input("Primer numero: "))
segundo_numero = int(input("Segundo numero: "))


opcion_correcta = False

while opcion_correcta == False:

    if operacion == "multiplicar":
        print("El resultado es: {}".format(primer_numero*segundo_numero))
        opcion_correcta = True
    elif operacion == "dividir":
        resul = float(primer_numero / segundo_numero)
        print("El resultado es: {}".format(resul))
        opcion_correcta = True
    elif operacion == "sumar":
        print("El resultado es: {}".format(primer_numero+segundo_numero))
        opcion_correcta = True
    elif operacion == "restar":
        if primer_numero < segundo_numero:
            print("El resultado es: {}".format(segundo_numero-primer_numero))
        else:
            print("El resultado es: {}".format(primer_numero-segundo_numero))
        opcion_correcta = True
    else:
        print("Debes elegir una operacion valida: ")