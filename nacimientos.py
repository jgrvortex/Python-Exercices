

lista_nacimientos = dict()

opcion = ""

while opcion != "S":
    opcion = input("Selecciona de las opciones disponibles la que deseas implementar: A para añadir un nuevo individuo, C para consultar o Salir para salir")

    if opcion == "A":
        nombre = input("Introduce el nombre de la persona: ")
        año_nacimiento = input("Introduce su año de nacimiento: ")
        lista_nacimientos[nombre] = año_nacimiento
    if opcion == "C":
        nombre = input("De quien quieres consultar su año de nacimiento?: ")
        print(lista_nacimientos[nombre])