


class Character:
    
    def attack(self, enemy):
        enemy.health -= self.power
    
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))

class Hero(Character):
    
    def __init__(self, name, hero_health, hero_power):
        self.name = name
        self.health = hero_health
        self.power = hero_power
            
    # def print_status(self):
    #     print("{} has {} health and {} power.".format(self.name, self.health, self.power))
    
class Goblin(Character):
    
    def __init__(self, name, goblin_health, goblin_power):
        self.name = name
        self.health = goblin_health
        self.power = goblin_power

class Zombie(Character):
    
    def __init__(self, name, zombie_health, zombie_power):
        self.name = name
        self.health = zombie_health
        self.power = zombie_power
        
    def alive(self):
        return True
        
you = str(input("Please enter your name: "))
hero = Hero(f'{you}: The Wonderful', 10, 5)

goblin = Goblin("The goblin", 6, 2)

zombie = Zombie("The zombie", 10, 1)

def main():

    while zombie.alive() and hero.alive():
        hero.print_status()
        zombie.print_status()
        print()
        print("What do you want to do?")
        print("1. fight zombie")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks zombie
            hero.attack(zombie)
            print("{} does {} damage to the zombie.".format(hero.name, hero.power))
            zombie.attack(hero)
            print("The zombie does {} damage to you.".format(zombie.power))
            if not zombie.alive():
                return True
        elif raw_input == "2":
            zombie.attack(hero)
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))
        
        if not hero.alive():
            print("You are dead.")

main()

