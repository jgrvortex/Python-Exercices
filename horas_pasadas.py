import datetime

year = int(input("Introduce el año: "))
month = int(input("Introduce el mes: "))
day = int(input("Introduce el dia: "))

ahora = datetime.datetime.now()
fecha = datetime.datetime(year=year, month=month, day=day)

tiempo_pasado = ahora - fecha
dias_pasados = tiempo_pasado.days

print("Han pasado {} horas desde esa fecha".format(dias_pasados * 24))