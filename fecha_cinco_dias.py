import datetime



semana = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]

dia_hoy = "viernes"

dia_hace_cinco = ""


hoy = datetime.datetime.now()

hace_cinco_dias = hoy - datetime.timedelta(days=5)

numdia = 0
for dias in semana:
    if dias == "viernes":
        break
    numdia += 1

dia_hace_cinco = semana[numdia-5]

print("Hace 5 dias fue {}, y el dia de la semana fue {}".format(hace_cinco_dias.strftime("%d del %m de %Y"),dia_hace_cinco))
