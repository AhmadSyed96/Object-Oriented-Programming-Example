class Pokimon:
    def __init__(self, name, level, type, max_health, health, isKnocked):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = max_health
        self.health = health
        self.isKnocked = isKnocked

    def print_name(self):
        print(self.name)

    def lose_health(self, decrease):
        print(f"decreasing health by {decrease}")
        self.health -= decrease
        print(f"your health is {self.health} now")
        if self.health <= 0:
            self.knock_out()

    def gain_health(self, increase):
        print(f"increasing health by {increase}")
        self.health += increase

    def knock_out(self):
        print("you've been knocked out")
        self.isKnocked = True
        self.health = 0

    def revive(self):
        self.isKnocked = False
        print("yove have been revived")

    def attack(self, pokimon2):
        two_x = {"fire": "grass", "water": "fire", "grass": "water"}
        half = {"fire": "water", "grass": "fire", "water": "grass"}
        if (self.type, pokimon2.type) in two_x.items():
            pokimon2.lose_health(2 * self.level)
            print("attack was SUPER effective")
        elif (self.type, pokimon2.type) in half.items():
            pokimon2.lose_health(float(0.5 * self.level))
            print("attack was NOT very effective")
        else:
            pokimon2.lose_health(self.level)
            print("attack was effective")



class Trainer():
    def __init__(self, name, pokimon, potions, active_pokimon):
        self.name = name
        self.pokimon = pokimon
        self.potions = potions
        self.active_pokimon = active_pokimon

    def use_potion(self):
        if self.active_pokimon.isKnocked == False:
            self.potions -= 1
            self.active_pokimon.gain_health(self.active_pokimon.max_health - self.active_pokimon.health)
            print(f"{self.active_pokimon.name} healed")
        else:
            print("pokimon is knocked")

    def attack_trainer(self, trainer2):
        self.active_pokimon.attack(trainer2.active_pokimon)
        print(f"trainer {self.name} attacked {trainer2.name}")

    def switch_pokimon(self):
        self.active_pokimon = self.pokimon.index(input("which pokimon do you want to use?"))


charizard = Pokimon("charizard", 2, "fire", 15, 10, False)
bulbasaur = Pokimon("bulbasaur", 5, "grass", 15, 10, False)
snorlax = Pokimon("snorlax", 3, "water", 12, 5, False)
squirtle = Pokimon("squirtle", 4, "water", 9, 20, False)

ash = Trainer("ash", [charizard, bulbasaur], 3, bulbasaur)
misty = Trainer("misty", [snorlax, squirtle], 1, squirtle)

ASH.attack_trainer(misty)
