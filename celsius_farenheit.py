
grados_celsius = -273

while (grados_celsius <= -273):

    grados_celsius = int(input("Introduce un valor termico en grados Celsius para convertirlos en grados Farenheit: "))

grados_farenheit = (float(grados_celsius) + 32) * 1.8

print("El valor en grados Farenheit es: {}".format(grados_farenheit))