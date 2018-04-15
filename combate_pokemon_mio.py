pokemon_elegido = input("¿Contra que Pokemon quieres combatir? (Squirtle, Charmander, Bulbasaur): ")


a_1 = 0
while a_1 == 0:

    if pokemon_elegido == "Squirtle":
        vida_enemigo = 90
        a_1 = 1
    elif pokemon_elegido == "Charmander":
        vida_enemigo = 80
        a_1 = 1
    elif pokemon_elegido == "Bulbasaur":
        vida_enemigo = 100
        a_1 = 1
    else:
        print("No has elegido un nombre correcto")

vida_pikachu = 100

while vida_pikachu > 0 and vida_enemigo > 0:

    a_2 = 0
    while a_2 == 0:
        ataque = input("Que tipo de ataque quieres emplear? (Chispazo, Bola Voltio): ")
        if ataque == "Chispazo":
            at = 1
            a_2 = 1
        elif ataque == "Bola Voltio":
            at = 2
            a_2 = 1
        else:
            print("Debes elegir uno de los dos ataques disponibles")
    if pokemon_elegido == "Squirtle":
        vida_pikachu -= 8
        if at == 1:
            vida_enemigo -= 10
        else:
            vida_enemigo -= 12
    elif pokemon_elegido == "Charmander":
        vida_pikachu -= 7
        if at == 1:
            vida_enemigo -= 10
        else:
            vida_enemigo -= 12
    elif pokemon_elegido == "Bulbasaur":
        vida_pikachu -= 10
        if at == 1:
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

