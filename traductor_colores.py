
lista_colores = {"blanco": "white", "negro": "black", "naranja": "orange", "gris": "grey", "marron": "brown", "granate": "maroon", "carmesi": "crimson", "verde": "green", "rojo": "red", "azul": "blue", "amarillo": "yellow"}


opcion = ""
color = ""

while opcion != "N":
    opcion = input("Quieres consultar la traduccion en ingles de algun color particular?: N (salir), S (consultar) ")
    if opcion == "N":
        break
    if opcion == "S":
        color = input("Indica el color del que quieres conocer su traduccion en ingles: ")
        print("La traduccion de {} es: {}".format(color,lista_colores[color]))
