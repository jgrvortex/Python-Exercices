

import random
from time import sleep

SECOND = 1

STR_1_1 = "Qué buen día hace hoy!"
STR_1_2 = "Me ha dicho que me quiere..."
STR_1_3 = "Hemos ganado el trofeo!"
STR_1_4 = "Por fin hemos alcanzado la cima del Monte Everest!"
STR_1_5 = "Me ha tocado la lotería!"

STR_2_1 = "Escritorio"
STR_2_2 = "Estantería"
STR_2_3 = "Armario"
STR_2_4 = "Ropero"
STR_2_5 = "Somier"

STR_3_1 = "Red Bull"
STR_3_2 = "Sidra El Gaitero"
STR_3_3 = "Fanta"
STR_3_4 = "Vichy Catalán"
STR_3_5 = "Vino"

STR_4_1 = "Cada día estoy más harto de ti"
STR_4_2 = "Ojalá te mueras"
STR_4_3 = "Deseo verle sufrir hasta el final"
STR_4_4 = "No quiero verte nunca más"
STR_4_5 = "Eres un ser despreciable"

STR_5_1 = "Gazpacho"
STR_5_2 = "Carpaccio"
STR_5_3 = "Salmón marinado"
STR_5_4 = "Cochinillo"
STR_5_5 = "Boquerones en vinagre"

STR_6_1 = "Otse on se anu esarf"
STR_6_2 = "Osto progonto no toono rosposto"
STR_6_3 = "--___ -- _ - __ --_-_-  __ - --- __ _-_-__---"
STR_6_4 = "Fraseando frases fraseadas fraseé fraseando frases"
STR_6_5 = "Persicali monicuslo menacoperiles plusminefico pelurico tacumerico"

STR_7_1 = "Gato"
STR_7_2 = "Camaleón"
STR_7_3 = "Mantis religiosa"
STR_7_4 = "Iguana"
STR_7_5 = "Cóndor"

STR_8_1 = "Lo estás consiguiendo!"
STR_8_2 = "Sólo tienes que caminar unos metros más para alcanzar la meta!"
STR_8_3 = "Has conseguido superar retos mucho más difíciles"
STR_8_4 = "Eres mucho más fuerte de lo que crees"
STR_8_5 = "Tienes capacidad para llegar mucho más alto!"

STR_9_1 = "Ladrido"
STR_9_2 = "Aullido"
STR_9_3 = "Graznido"
STR_9_4 = "Zumbido"
STR_9_5 = "Maullido"

STR_10_1 = "Nunca más volveré a verla..."
STR_10_2 = "Cuánto la echo de menos!"
STR_10_3 = "El otro día murió nuestro amigo"
STR_10_4 = "El pobre pereció mientras lo abrazaba su madre"
STR_10_5 = "No va a conseguir sobrevivir..."

list_happy = [STR_1_1,STR_1_2,STR_1_3,STR_1_4,STR_1_5]
list_furniture = [STR_2_1,STR_2_2,STR_2_3,STR_2_4,STR_2_5]
list_drink = [STR_3_1,STR_3_2,STR_3_3,STR_3_4,STR_3_5]
list_hate = [STR_4_1,STR_4_2,STR_4_3,STR_4_4,STR_4_5]
list_food = [STR_5_1,STR_5_2,STR_5_3,STR_5_4,STR_5_5]
list_absurd = [STR_6_1,STR_6_2,STR_6_3,STR_6_4,STR_6_5]
list_animal = [STR_7_1,STR_7_2,STR_7_3,STR_7_4,STR_7_5]
list_motivation = [STR_8_1,STR_8_2,STR_8_3,STR_8_4,STR_8_5]
list_animal_sound = [STR_9_1,STR_9_2,STR_9_3,STR_9_4,STR_9_5]
list_sad = [STR_10_1,STR_10_2,STR_10_3,STR_10_4,STR_10_5]

list_of_lists = [list_happy,list_furniture,list_drink,list_hate,list_food,list_absurd,list_animal,list_motivation,list_animal_sound,list_sad]

count_second = 1

while True:
    for sec in range(0,9):
        string_number = random.randint(0,4)
        second_module = count_second % 10
        aux_list = list_of_lists[second_module]
        print(aux_list[string_number])
        sleep(SECOND)
        count_second += 1