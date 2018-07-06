from combate_pokemon.Pokemon import Charmander, Squirtle, Bulbasaur, Pikachu


def chosen_enemy():

    chosen_pokemon = input("¿Contra que Pokemon quieres combatir? (1 - Squirtle, 2- Charmander, 3- Bulbasaur): ")

    correct_choice = False
    while correct_choice == False:

        if chosen_pokemon == "1":
            pokemon_enemy = Squirtle()
            print("De acuerdo. {} será tu oponente".format(Squirtle.name))
            correct_choice = True
        elif chosen_pokemon == "2":
            pokemon_enemy = Charmander()
            print("De acuerdo. {} será tu oponente".format(Charmander.name))
            correct_choice = True
        elif chosen_pokemon == "3":
            pokemon_enemy = Bulbasaur()
            print("De acuerdo. {} será tu oponente".format(Bulbasaur.name))
            correct_choice = True
        else:
            print("No has elegido un nombre correcto")

    return pokemon_enemy


def fight(my_pokemon, pokemon_enemy):

    while my_pokemon.life > 0 and pokemon_enemy.life > 0:

        correct_choice = False
        while correct_choice == False:
            attack_choice = input("Elige el ataque: (1 - Chispazo, 2 - Bola Voltio): ")
            if attack_choice == "1" or attack_choice == "2":
                correct_choice = True
            else:
                print("Debes elegir uno de los dos ataques disponibles")

        my_pokemon.receive_pain(pokemon_enemy.pain_attack)
        pokemon_enemy.receive_pain(attack_choice)


        if my_pokemon.life > 0 and pokemon_enemy.life > 0:
            print("El estado del combate es el siguiente: Pikachu - Vida: {}   ".format(my_pokemon.life) + pokemon_enemy.name + " - Vida: {}".format(pokemon_enemy.life))
        else:
            if my_pokemon.life <= 0 and pokemon_enemy.life > 0:
                print(pokemon_enemy + " ha ganado la batalla!!")
            elif my_pokemon.life > 0 and pokemon_enemy.life <= 0:
                print("Pikachu ha ganado la batalla!!")
            else:
                print("Se ha producido un empate!!")

def main():
    my_pokemon = Pikachu()
    enemy = chosen_enemy()
    fight(my_pokemon, enemy)


if __name__ == "__main__":
    main()

