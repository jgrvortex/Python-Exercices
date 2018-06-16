
import datetime
import random

AVERAGE_LIFESPAN = 80

SMOKER_PENALIZATION = 10
DRINKER_PENALIZATION = 10
SEDENTARY_PENALIZATION = 20
DISEASE_PENALIZATION = 15
FAMILY_EARLY_DEATH_PENALIZATION = 24
HEALTHY_DIET_PENALIZATION = 20
TEMERARY_PENALIZATION = 20
SUICIDE_TENDENCY_PENALIZATION = 20
RISK_PROFESSION_PENALIZATION = 10

QUESTION_1 = "¿Fumas? "
QUESTION_2 = "¿Bebes? "
QUESTION_3 = "¿Haces ejercicio? "
QUESTION_4 = "¿Padeces alguna enfermedad grave? Indica su gravedad: "
QUESTION_5 = "Indica el numero de familiares que hayan muerto jovenes: "
QUESTION_6 = "¿Sigues una dieta saludable y equilibrada? "
QUESTION_7 = "¿Eres una persona temeraria? "
QUESTION_8 = "¿Tienes pensamientos suicidas frecuentemente? "
QUESTION_9 = "¿Ejerces una profesion peligrosa? "



def ask_how_much(message,penalization):
    response = None
    while response not in range(0,5):
        response = int(input(message + "  [4: mucho, 3: bastante, 2: moderado, 1: poco, 0: nada] "))
    if response == 4:
        return penalization * 100 / 100
    elif response == 3:
        return penalization * 75 / 100
    elif response == 2:
        return penalization * 50 / 100
    elif response == 1:
        return penalization * 25 / 100
    elif response == 0:
        return 0


def print_with_underscores(message):
    print(message)
    print(len(message) * "-")

print_with_underscores("Averigua cuanto te queda de vida")
print("Completa estas preguntas para calcular tu tiempo de vida restante")

birth_date = input("Cual es tu fecha de nacimiento (formato: dd/mm/yyyy): ? ")

birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")


base_lifespan = random.randint(AVERAGE_LIFESPAN/2, AVERAGE_LIFESPAN)

years_lost = 0

list_penalizations = [SMOKER_PENALIZATION,DRINKER_PENALIZATION,SEDENTARY_PENALIZATION,DISEASE_PENALIZATION,FAMILY_EARLY_DEATH_PENALIZATION,HEALTHY_DIET_PENALIZATION,TEMERARY_PENALIZATION,SUICIDE_TENDENCY_PENALIZATION,RISK_PROFESSION_PENALIZATION]
list_questions = [QUESTION_1,QUESTION_2,QUESTION_3,QUESTION_4,QUESTION_5,QUESTION_6,QUESTION_7,QUESTION_8,QUESTION_9]

for question_number in range(0,9):
    message = list_questions[question_number]
    penalization = list_penalizations[question_number]
    years_lost += (base_lifespan - years_lost) * ask_how_much(message,penalization) / 100

lifespan = base_lifespan - years_lost

death_day = birth_date + datetime.timedelta(days=lifespan*365)
days_to_death = death_day - datetime.datetime.now()

print("Fecha de tu muerte: {}".format(death_day.strftime("%d/%m/%Y")))
print("Faltan {} dias para tu muerte".format(days_to_death.days))