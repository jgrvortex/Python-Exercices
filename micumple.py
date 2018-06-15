import datetime



semana = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]

dia_hoy = "viernes"

dia_cumpleanos = ""


hoy = datetime.datetime.now()

cumpleanos = datetime.datetime(year=2019, month=5, day=30)

tiempo_cumpleanos = cumpleanos - hoy
dias_cumpleanos = tiempo_cumpleanos.days + 1
#Hay que sumarle un día más porque sino el día de hoy, que no es completo por haberse iniciado ya, no sería sumado en el total de días

numdia = 0
for dias in semana:
    if dias == "viernes":
        break
    numdia += 1

ndias = dias_cumpleanos % 7
if ndias + numdia > 7:
    dia_cumpleanos = semana[numdia - (7 - ndias)]
else:
    dia_cumpleanos = semana[numdia + ndias]

print("Para mi proximo cumpleaños faltan {} dias, y el dia de la semana sera {}".format(dias_cumpleanos,dia_cumpleanos))