
from time import sleep
import datetime

NIGHT_STARTS = 21
DAY_STARTS = 7
HOUR_DURATION = 1



def write_file_and_screen(text,file_name):
    with open(file_name, "a") as hours_file:
        hours_file.write("{}{}".format(text, "\n"))
        print(text)


def main():

    alarm_days = []
    count_day = 0
    current_time = datetime.datetime.now()
    alarm_hour = -1
    alarm_date = "00/00/0000"
    current_time_formatted = "00/00/1111"

    is_night = False
    date_ok = False

    activator_2 = "N"
    activator_3 = "N"


    activator_1 = input("¿Deseas activar una alarma? S/N ")
    if activator_1 == "N":
        pass
    elif activator_1 == "S":
        while alarm_hour < 0 or alarm_hour > 24:
            alarm_hour = int(input("Introduce la hora de la alarma: "))
        activator_2 = input("¿Deseas que la alarma suene un día particular de la semana? S/N ")
        if activator_2 == "N":
            activator_3 = input("¿Deseas que la alarma suene en una fecha determinada? S/N ")
            if activator_3 == "N":
                pass
            else:
                alarm_date = input("Introduce la fecha en la que sonará la alarma: (formato: dd/mm/yyyy): " )
                alarm_date = datetime.datetime.strptime(alarm_date, "%d/%m/%Y")
                date_ok = True
        elif activator_2 == "S":

            alarm_weekday = 1
            how_many_days = 0
            today = int(input("Introduce el día de la semana actual: (1-lunes,2-martes,3-miércoles,4-jueves,5-viernes,6-sábado,7-domingo) "))

            while (alarm_weekday > 0 and alarm_weekday < 8):
                alarm_weekday = int(input("Introduce el día de la semana en el que sonará la alarma: (1-lunes,2-martes,3-miércoles,4-jueves,5-viernes,6-sábado,7-domingo,0-no introducir más días) "))
                if alarm_weekday == 0:
                    break
                if alarm_weekday in alarm_days:
                    continue
                alarm_days.append(alarm_weekday)
                how_many_days += 1
                #Como el día de la semana en que se está escribiendo este programa es domingo y a éste se le adjudica el número 7, y el que día siguiente sería lunes y
                # su valor sería el 1, podemos identificar a los días de la semana futuros haciendo el módulo entre los días transcurridos desde hoy (poniendo el contador
                # count_day a 0) y el número de día asignado a cada día de la semana (lunes = 1, martes = 2, etc)

    count_day += today
    is_the_day = False

    while True:
        sleep(HOUR_DURATION)
        current_time += datetime.timedelta(hours=1)
        #print("La hora actual es: {}".format(current_time))
        light_changed = False

        if (current_time.hour >= NIGHT_STARTS or current_time.hour <= DAY_STARTS) and not is_night:
            day_night_label = "Noche"
            is_night = True
            light_changed = True
        elif (current_time.hour > DAY_STARTS and current_time.hour < NIGHT_STARTS) and is_night:
            day_night_label = "Día"
            is_night = False
            light_changed = True

        #print("La hora actual es: {} y es de {}".format(current_time,day_night_label))
        #with open("horas.txt", "a") as hours_file:
            #time_text = "La hora actual es: {}\n".format(current_time)

        if light_changed:
            if is_night:
                write_file_and_screen("Se ha hecho de noche", "horas.txt")
                #hours_file.write("Se ha hecho de noche")
            else:
                write_file_and_screen("Se ha hecho de día", "horas.txt")
                #hours_file.write("Se ha hecho de día")


        if current_time.hour % 24 == 0:
            count_day += 1

        for num in range(0, how_many_days):
            if alarm_days[num] < count_day:
                alarm_days[num] += 7
            elif alarm_days[num] == count_day:
                is_the_day = True
                alarm_days[num] += 7


        if date_ok == True:
            current_time_formatted = datetime.datetime.strptime(current_time,"%d/%m/%Y")

        activation_1 = False
        activation_2 = False
        activation_3 = False

        if (activator_1 == "S" and activator_2 == "N" and activator_3 == "N"):
            activation_1 = True
        if (activator_1 == "S" and activator_2 == "S" and activator_3 == "N"):
            activation_2 = True
        if (activator_1 == "S" and activator_2 == "N" and activator_3 == "S" and date_ok == True):
            activation_3 = True


        alarm_option_1 = False
        alarm_option_2 = False
        alarm_option_3 = False

        if ((alarm_hour == current_time.hour) and activation_1):
            alarm_option_1 = True
        if ((alarm_hour == current_time.hour and is_the_day == True) and activation_2):
            alarm_option_2 = True
        if ((alarm_hour == current_time.hour and alarm_date == current_time_formatted) and activation_3):
            alarm_option_3 = True


        if ((alarm_option_1 == True) or (alarm_option_2 == True) or (alarm_option_3 == True)):
            print("\n")
            is_the_day = False
        else:
            write_file_and_screen("La hora actual es: {}".format(current_time), "horas.txt")
            print("{}".format(count_day))
            for num in range(0, how_many_days):
                dayofalarm = alarm_days[num]
                print("{}".format(dayofalarm))

            #hours_file.write(time_text)
            #print(text_time)


            #hours_file.write("La hora actual es: {} y es de {}\n".format(current_time,day_night_label))

#with open("horas.txt","w") as hours_file:
#    hours_file.write("Hola")

#Otra manera de abrir, escribir y cerrar archivo
#hours_file = open("horas.txt", "x")
#hours_file.write("Hola")
#hours_file.close()

if __name__ == "__main__":
    main()
