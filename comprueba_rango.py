

numero = 4425

minimo = 1000

maximo = 10000

def numero_en_rango(num, min, max):
    dentro_rango = False
    if numero >= min and numero <= max:
        dentro_rango = True
    return dentro_rango

dentro = numero_en_rango(numero, minimo, maximo)

if dentro == True:
    print("El numero {} esta contenido en el intervalo limitado por {} y {}".format(numero,minimo,maximo))
if dentro == False:
    print("El numero {} esta contenido en el intervalo limitado por {} y {}".format(numero, minimo, maximo))