

import random
from time import sleep

SECONDS = 3

STR_1 = "De aquí poco empezará el verano"
STR_2 = "Esto es un ejercicio de programación"
STR_3 = "Hace tiempo vi un coche volador"
STR_4 = "Pronto mi habitación estará totalmente reformada"
STR_5 = "Tengo que examinarme en poco tiempo"
STR_6 = "Esta frase tiene cinco palabras"
STR_7 = "No me gustaría tener que rescatarte de esas criaturas"
STR_8 = "Aquí vivía un monstruo marino hace mucho tiempo"
STR_9 = "Me comentó que el otro día vio un OVNI"
STR_10 = "Creo que ya no está enfermo"


string_list = [STR_1,STR_2,STR_3,STR_4,STR_5,STR_6,STR_7,STR_8,STR_9,STR_10]

while True:
    string_number = random.randint(0, 9)
    string_to_print = string_list[string_number]
    print(string_to_print)
    sleep(SECONDS)