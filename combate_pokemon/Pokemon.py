
class BasePokemon:

    life = 100
    pain_attack = 10
    name = "Pokemon"

    def __init__(self):
        self.life = self.base_life

    def receive_pain(self, attack_choice):
        pain_attack_1 = 10
        pain_attack_2 = 15
        if attack_choice == "1":
            self.pain_attack = pain_attack_1
        if attack_choice == "2":
            self.pain_attack = pain_attack_2
        self.life -= self.pain_attack

    def show_life(self):
        print("Vida de {}: {}".format(self.name, self.life))



class Pikachu(BasePokemon):

    base_life = 120

    def receive_pain(self, pain_attack):
        self.life -= pain_attack

    name = "Pikachu"


class Charmander(BasePokemon):

    base_life = 100
    pain_attack = 10
    name = "Charmander"


class Bulbasaur(BasePokemon):

    base_life = 90
    pain_attack = 7
    name = "Bulbasaur"


class Squirtle(BasePokemon):

    base_life = 80
    pain_attack = 15
    name = "Squirtle"


