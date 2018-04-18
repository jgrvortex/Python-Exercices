pokemon_elegido = input("¿Contra que Pokemon quieres combatir? (Squirtle, Charmander, Bulbasaur): ")


eleccion_correcta_1 = False
while eleccion_correcta_1 == False:

    if pokemon_elegido == "Squirtle":
        vida_enemigo = 90
        eleccion_correcta_1 = True
    elif pokemon_elegido == "Charmander":
        vida_enemigo = 80
        eleccion_correcta_1 = True
    elif pokemon_elegido == "Bulbasaur":
        vida_enemigo = 100
        eleccion_correcta_1 = True
    else:
        print("No has elegido un nombre correcto")

vida_pikachu = 100

while vida_pikachu > 0 and vida_enemigo > 0:

    eleccion_correcta_2 = False
    while eleccion_correcta_2 == False:
        ataque = input("Que tipo de ataque quieres emplear? (Chispazo, Bola Voltio): ")
        if ataque == "Chispazo":
            tipo_ataque = 1
            eleccion_correcta_2 = True
        elif ataque == "Bola Voltio":
            tipo_ataque = 2
            eleccion_correcta_2 = False
        else:
            print("Debes elegir uno de los dos ataques disponibles")
    if pokemon_elegido == "Squirtle":
        vida_pikachu -= 8
        if tipo_ataque == 1:
            vida_enemigo -= 10
        else:
            vida_enemigo -= 12
    elif pokemon_elegido == "Charmander":
        vida_pikachu -= 7
        if tipo_ataque == 1:
            vida_enemigo -= 10
        else:
            vida_enemigo -= 12
    elif pokemon_elegido == "Bulbasaur":
        vida_pikachu -= 10
        if tipo_ataque == 1:
            vida_enemigo -= 10
        else:
            vida_enemigo -= 12

    if vida_enemigo > 0 and vida_pikachu > 0:
        print("El estado del combate es el siguiente: Pikachu - Vida: {}   ".format(vida_pikachu) + pokemon_elegido + " - Vida: {}".format(vida_enemigo))
    else:
        if vida_pikachu <= 0 and vida_enemigo > 0:
            print(pokemon_elegido + " ha ganado la batalla!!")
        elif vida_pikachu > 0 and vida_enemigo <= 0:
            print("Pikachu ha ganado la batalla!!")
        else:
            print("Se ha producido un empate!!")

