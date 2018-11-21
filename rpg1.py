## Character template class
class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    ## checks health of characters
    def alive(self):
        if self.name == "zombie":
            return True
        elif self.health > 0:
            return True
        else:
            return False
    ## prints health and power of character
    def print_status(self):
        if self.name == "zombie":
            print(f"{self.name} => health: infinite | power: {self.power}")
        else:
            print(f"{self.name} => health: {self.health} | power: {self.power}")
    ## attack damage
    def attack(self, enemy):
        enemy.health -= self.power
        print(f"{self.name} does {self.power} damage to {enemy.name}")
        if enemy.health <= 0 and enemy.name != "zombie":
            print(f"{enemy.name} is dead.")
        if self.health <= 0:
            print(f"{self.name} is dead.")
## individual Character classes
class Hero(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
                
class Goblin(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

class Zombie(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

## Start of game
def main():       
    hero = Hero("hero", 10, 5)
    goblin = Goblin("goblin", 6, 2)
    zombie = Zombie("zombie",100, 4)

    while zombie.alive() and hero.alive():
        hero.print_status()
        zombie.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=" ")
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(zombie)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else: print("Invalid input {}" .format(raw_input))

        if zombie.alive():
            # Zombie attacks hero
            zombie.attack(hero)

main()