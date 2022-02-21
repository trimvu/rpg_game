
import random

#! CHARACTER CLASS
class Character:
    
    def attack(self, enemy):
        enemy.health -= self.power
    
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
    def print_status(self):
        print("{} has {} health and {} power and {} evade and {} armor modifier.".format(self.name, self.health, self.power, self.evade, self.modifier))
#! HERO CLASS
class Hero(Character):
    
    def __init__(self, name, hero_health, hero_power):
        self.name = name
        self.health = hero_health
        self.power = hero_power
        self.coins = 50
        self.inventory = []
        self.armor = []
        self.weapon = []
        self.modifier = 0
        self.evade = 0
    
    def attack2(self, enemy):
        r = random.randint(1, 5)
        if r == 3:
            enemy.health -= (self.power * 2)
            print("{} does {} damage to the {}.".format(hero.name, (self.power * 2), enemy.name))
        else:
            enemy.health -= self.power
            print("{} does {} damage to the {}.".format(hero.name, hero.power, enemy.name))
            
    def purse(self, bounty):
        self.coins += bounty
        
    def getInventory(self):
        for objects in self.inventory:
            print(objects)
    
    def addItems(self, item, cost):
        if hero.coins >= cost:
            hero.inventory.append(item)
            self.coins -= cost
        else:
            print("Insufficent funds.")
            
    def heroEvade(self, enemy):
        if self.evade == 0:
            self.health -= (enemy.power * (1 - self.modifier))
            print("{} does {} damage to you.".format(enemy.name, (enemy.power * (1 - self.modifier))))
        elif self.evade == 2:
            r = random.randint(1, 20)
            if r == 6:
                self.health = self.health
                print("{} has evaded {}'s attack".format(self.name, enemy.name))
            else:
                self.health -= (enemy.power * (1 - self.modifier))
                print("{} does {} damage to you.".format(enemy.name, enemy.power))
        elif self.evade == 4:
            r = random.randint(1, 10)
            if r == 8:
                self.health = self.health
                print("{} has evaded {}'s attack".format(self.name, enemy.name))
            else:
                self.health -= (enemy.power * (1 - self.modifier))
                print("{} does {} damage to you.".format(enemy.name, enemy.power))
        elif self.evade == 6:
            r = random.randint(1, 20)
            if r == 5 or r == 10 or r == 15:
                self.health = self.health
                print("{} has evaded {}'s attack".format(self.name, enemy.name))
            else:
                self.health -= (enemy.power * (1 - self.modifier))
                print("{} does {} damage to you.".format(enemy.name, enemy.power))
        elif self.evade == 8:
            r = random.randint(1, 40)
            if r == 2 or r == 3 or r == 5 or r == 7 or r == 17 or r == 23 or r == 31:
                self.health = self.health
                print("{} has evaded {}'s attack".format(self.name, enemy.name))
            else:
                self.health -= (enemy.power * (1 - self.modifier))
                print("{} does {} damage to you.".format(enemy.name, enemy.power))
        elif self.evade >= 10:
            r = random.randint(1, 5)
            if r == 3:
                self.health = self.health
                print("{} has evaded {}'s attack".format(self.name, enemy.name))
            else:
                self.health -= (enemy.power * (1 - self.modifier))
                print("{} does {} damage to you.".format(enemy.name, enemy.power))

#! GOBLIN CLASS
class Goblin(Character):
    
    def __init__(self, name, goblin_health, goblin_power):
        self.name = name
        self.health = goblin_health
        self.power = goblin_power
        self.coins = 5
        self.modifier = 0
        self.evade = 0
        
    def bounty(self):
        return self.coins
#! ZOMBIE CLASS
class Zombie(Character):
    
    def __init__(self, name, zombie_health, zombie_power):
        self.name = name
        self.health = zombie_health
        self.power = zombie_power
        self.coins = 0
        self.modifier = 0
        self.evade = 0
        
    # def alive(self):
        # return True
    
    def bounty(self):
        return self.coins
#! MEDIC CLASS
class Medic(Character):
    
    def __init__(self, name, medic_health, medic_power):
        self.name = name
        self.health = medic_health
        self.power = medic_power
        self.coins = 6
        self.modifier = 0
        self.evade = 0
        
    def heal(self):
        r = random.randint(1, 5)
        if r == 2:
            self.health += 2
            print("The medic gained 2 health")
        else:
            self.health == self.health
            
    def bounty(self):
        return self.coins
#! SHADOW CLASS
class Shadow(Character):
    
    
    def __init__(self, name, shadow_health, shadow_power):
        self.name = name
        self.health = shadow_health
        self.power = shadow_power
        self.coins = 7
        self.modifier = 0
        self.evade = 0
        
    def no_damage(self, enemy):
        r = random.randint(1, 10)
        if r == 7:
            self.health -= enemy.power
            print("{} does {} damage to the shadow.".format(hero.name, hero.power))
        else:
            self.health == self.health
            print("{} does no damage to the shadow.".format(hero.name))
        
    def bounty(self):
        return self.coins
#! KNIGHT CLASS
class Knight(Character):
    
    def __init__(self, name, knight_health, knight_power):
        self.name = name
        self.health = knight_health
        self.power = knight_power
        self.coins = 10
        self.modifier = 0.125
        self.evade = 0
        
    def bounty(self):
        return self.coins
#! ITEMS CLASS      
class Items:
    def __init__(self, name, cost, mod):
        self.name = name
        self.cost = cost
        self.mod = mod
        
    def price(self):
        return self.cost
    
    def __str__(self):
        return self.name
#! SUPER TONIC CLASS
class Super_tonic(Items):
    def __init__(self):
        self.name = "Super Tonic"
        self.cost = 10
        
    def heal(self, hero):
        hero.health = 10
        
        
#! HELM CLASS
class Helm(Items):
    def __init__(self):
        self.name = "Helmet"
        self.cost = 75
        self.mod = 0.05
        
    def equipped(self, hero):
        hero.modifier += self.mod
        
#! CHEST ARMOR CLASS
class ChestArmor(Items):
    def __init__(self):
        self.name = "Chest Plate"
        self.cost = 150
        self.mod = 0.1
        
    def equipped(self, hero):
        hero.modifier += self.mod
        
#! GAUNTLETS CLASS
class Gauntlets(Items):
    def __init__(self):
        self.name = "Gauntlets"
        self.cost = 38
        self.mod = 0.025
        
    def equipped(self, hero):
        hero.modifier += self.mod
        
#! LEGGINGS CLASS
class Leggings(Items):
    def __init__(self):
        self.name = "Leggings"
        self.cost = 113
        self.mod = 0.075
   
    def equipped(self, hero):
        hero.modifier += self.mod
   
#! EVADE CLASS
class Evade(Items):
    def __init__(self):
        self.name = "Evade"
        self.cost = 50
        
    def evadeAttack(self, hero):
        hero.evade += 2
#! SWORD CLASS
class Sword(Items):
    def __init__(self):
        self.name = "Sword"
        self.cost = 100
    
    def boostAttack(self, hero):
        hero.power += 2
#! DIE
class Die(Items):
    def __init__(self):
        self.name = "Die Zombie"
        self.cost = 250
        
    def dieZombie(self, zombie):
        zombie.health = 0
        
you = str(input("Please enter your name: "))
hero = Hero(f'{you}: The Great', 10, 5)

goblin = Goblin("The goblin", 6, 2)

zombie = Zombie("The zombie", 10, 1)

medic = Medic("The medic", 7, 2)

shadow = Shadow("The shadow", 1, 1)

knight = Knight("The knight", 15, 5)

supertonic = Super_tonic()

helmet = Helm()

chestplate = ChestArmor()

gauntlets = Gauntlets()

leggings = Leggings()

evade = Evade()

sword = Sword()

die = Die()

#! LOBBY
def lobby():
    
    while hero.alive():
        hero.print_status()
        print()
        print("{} arrives at a village. Where would you like to go?".format(hero.name))
        print("1. The Gauntlet")
        print("2. Store")
        print("3. Items")
        print("4. View Armor")
        print("5. View Weapon")
        print("6. Quit. Warning: NO SAVE")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            theGauntlet() 
        elif raw_input == "2":
            store()
        elif raw_input == "3":
            equipItems()
        elif raw_input == "4":
            print("\nThe armor you are currently wearing: \n")
            for x in hero.armor:
                print(x)
            print()
        elif raw_input == "5":
            print("\nThe weapon you are currently holding: \n")
            for x in hero.weapon:
                print(x)
            print()
        elif raw_input == "6":
            print("Quitter...")
            quit()
        elif raw_input == "7":
            zombieFight()
        else:
            print("Invalid input {}".format(raw_input))            

#! The Gauntlet
def theGauntlet():
    
    while hero.alive():
        hero.print_status()
        print("\n {} enters the village to the sight of a goblin. How would you like to proceed?".format(hero.name))
        print("1. Fight the goblin")
        print("2. Go back to the village entrance")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            if not goblin.alive():
                goblin.health = 6
            goblinFight()
        elif raw_input == "2":
            lobby()
        while hero.alive():
            hero.print_status()
            print("\n {} slays the goblin. A medic arrives to aid the goblin. How would you like to proceed?".format(hero.name))
            print("1. Fight the medic")
            print("2. Go back to the village entrance")
            print("> ", end=' ')
            raw_input = input()
            if raw_input == "1":
                if not medic.alive():
                    medic.health = 7
                medicFight()
            elif raw_input == "2":
                lobby()
            while hero.alive():
                hero.print_status()
                print("\n {} slays the medic. A shadow appears. How would you like to proceed?".format(hero.name))
                print("1. Fight the shadow")
                print("2. Go back to the village entrance")
                print("> ", end=' ')
                raw_input = input()
                if raw_input == "1":
                    if not shadow.alive():
                        shadow.health = 1
                    shadowFight()
                elif raw_input == "2":
                    lobby()
                while hero.alive():
                    hero.print_status()
                    print("\n {} slays the shadow. A knight charges at you. How would you like to proceed?".format(hero.name))
                    print("1. Fight the knight")
                    print("2. Go back to the village entrance")
                    print("> ", end=' ')
                    raw_input = input()
                    if raw_input == "1":
                        if not knight.alive():
                            knight.health = 10
                        knightFight()
                    elif raw_input == "2":
                        lobby()
                    while hero.alive():
                        hero.print_status()
                        print("\n {} slays the knight. The knight reanimates into a zombie. How would you like to proceed?".format(hero.name))
                        print("1. Fight the zombie")
                        print("2. Go back to the village entrance")
                        print("> ", end=' ')
                        raw_input = input()
                        if raw_input == "1":
                            if not zombie.alive():
                                zombie.health = 10
                            zombieFight()
                        elif raw_input == "2":
                            lobby()
                        while hero.alive():
                            hero.print_status()
                            print("\n{} slays the zombie. You just committed genocide on an innocent village.".format(hero.name))
                            print("{}? There's nothing great about being a butcher.".format(hero.name))
                            print("YOU WIN.")
                            quit()
    

#! GOBLIN
def goblinFight():

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. Fight goblin")
        print("2. Do nothing")
        print("3. Items")
        print("4. Flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack2(goblin)
            # print("{} does {} damage to the goblin.".format(hero.name, hero.power))
            hero.heroEvade(goblin)
            # print("The goblin does {} damage to you.".format(goblin.power))
            if not goblin.alive():
                hero.purse(goblin.bounty())
                print("The goblin is dead.")
                print("The goblin dropped {} coins".format(goblin.bounty()))
                print("{} now has {} coins".format(hero.name, hero.coins))
        elif raw_input == "2":
            hero.heroEvade(goblin)
        elif raw_input == "3":
            equipItems()
        elif raw_input == "4":
            print("{} fled.".format(hero.name))
            break
        else:
            print("Invalid input {}".format(raw_input))
        
        if not hero.alive():
            print("You are dead.")
        

#! MEDIC
def medicFight():

    while medic.alive() and hero.alive():
        hero.print_status()
        medic.print_status()
        print()
        print("What do you want to do?")
        print("1. Fight medic")
        print("2. Do nothing")
        print("3. Items")
        print("4. Flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks medic
            
            hero.attack2(medic)
            # print("{} does {} damage to the medic.".format(hero.name, hero.power))
            medic.heal()
            hero.heroEvade(medic)
            # print("The medic does {} damage to you.".format(medic.power))
            if not medic.alive():
                hero.purse(medic.bounty())
                print("The medic is dead.")
                print("The medic dropped {} coins".format(medic.bounty()))
                print("{} now has {} coins".format(hero.name, hero.coins))
        elif raw_input == "2":
            medic.heal()
            hero.heroEvade(medic)
            print("The medic does {} damage to you.".format(medic.power))
        elif raw_input == "3":
            equipItems()
        elif raw_input == "4":
            print("{} fled.".format(hero.name))
            break
        else:
            print("Invalid input {}".format(raw_input))
        
        if not hero.alive():
            print("You are dead.")
            
            
#! SHADOW
def shadowFight():

    while shadow.alive() and hero.alive():
        hero.print_status()
        shadow.print_status()
        print()
        print("What do you want to do?")
        print("1. Fight shadow")
        print("2. Do nothing")
        print("3. Items")
        print("4. Flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks shadow
            
            shadow.no_damage(hero)
            
            hero.heroEvade(shadow)
            # print("The shadow does {} damage to you.".format(shadow.power))
            if not shadow.alive():
                hero.purse(shadow.bounty())
                print("The shadow is dead.")
                print("The shadow dropped {} coins".format(shadow.bounty()))
                print("{} now has {} coins".format(hero.name, hero.coins))
        elif raw_input == "2":
            hero.heroEvade(shadow)
            print("The shadow does {} damage to you.".format(shadow.power))
        elif raw_input == "3":
            equipItems()
        elif raw_input == "4":
            print("{} fled.".format(hero.name))
            break
        else:
            print("Invalid input {}".format(raw_input))
        
        if not hero.alive():
            print("You are dead.")
            
            
#! ZOMBIE
def zombieFight():

    while zombie.alive() and hero.alive():
        hero.print_status()
        zombie.print_status()
        print()
        print("What do you want to do?")
        print("1. Fight zombie")
        print("2. Do nothing")
        print("3. Items")
        print("4. Flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks zombie
            # hero.attack2(zombie)
            # print("{} does {} damage to the zombie.".format(hero.name, hero.power))
            hero.heroEvade(zombie)
            print("The zombie does {} damage to you.".format(zombie.power))
            # if not zombie.alive():
            #     return True
        elif raw_input == "2":
            hero.heroEvade(zombie)
        elif raw_input == "3":
            equipItems()
        elif raw_input == "4":
            print("{} fled.".format(hero.name))
            break
        else:
            print("Invalid input {}".format(raw_input))
        
        if not hero.alive():
            print("You are dead.")
            
#! KNIGHT
def knightFight():

    while knight.alive() and hero.alive():
        hero.print_status()
        knight.print_status()
        print()
        print("What do you want to do?")
        print("1. Fight knight")
        print("2. Do nothing")
        print("3. Items")
        print("4. Flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks knight
            hero.attack2(knight)
            # print("{} does {} damage to the knight.".format(hero.name, hero.power))
            hero.heroEvade(knight)
            # print("The knight does {} damage to you.".format(knight.power))
            if not knight.alive():
                hero.purse(knight.bounty())
                print("The knight is dead.")
                print("The knight dropped {} coins".format(knight.bounty()))
                print("{} now has {} coins".format(hero.name, hero.coins))
        elif raw_input == "2":
            hero.heroEvade(knight)
        elif raw_input == "3":
            equipItems()
        elif raw_input == "4":
            print("{} fled.".format(hero.name))
            break
        else:
            print("Invalid input {}".format(raw_input))
        
        if not hero.alive():
            print("You are dead.")
            

#! STORE
def store():

    while hero.alive():
        hero.print_status()
        print()
        print("What would you like to purchase?")
        print("{}'s coin balance: {}".format(hero.name, hero.coins))
        print("1. Super Tonic: Restores HP back to 10. Cost: {} coins".format(supertonic.price()))
        print("2. Helmet: Reduces damage taken from enemies by 5%. Cost: {} coins".format(helmet.price()))
        print("3. Chest Armor: Reduces damage taken from enemies by 10%. Cost: {} coins".format(chestplate.price()))
        print("4. Gauntlets: Reduces damage taken from enemies by 2.5%. Cost: {} coins".format(gauntlets.price()))
        print("5. Leggings: Reduces damage taken from enemies by 7.5%. Cost: {} coins".format(leggings.price()))
        print("6. Evade: Increases your chance to dodge an attack. Cost: {} coins".format(evade.price()))
        print("7. Sword: Increases your power by 2. Cost: {} coins".format(sword.price()))
        print("8. Die, Zombie: Item needed to kill the zombie")
        print("9. Return to village entrance.")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.addItems(supertonic, supertonic.price())
        elif raw_input == "2":
            hero.addItems(helmet, helmet.price())
        elif raw_input == "3":
            hero.addItems(chestplate, chestplate.price())
        elif raw_input == "4":
            hero.addItems(leggings, leggings.price())
        elif raw_input == "5":
            hero.addItems(gauntlets, gauntlets.price())
        elif raw_input == "6":
            hero.addItems(evade, evade.price())
        elif raw_input == "7":
            hero.addItems(sword, sword.price())
        elif raw_input == "8":
            hero.addItems(die, die.price())
        elif raw_input == "9":
            break
        

#! ITEMS VIEW AND EQUIP
def equipItems():
    hero.print_status()
    print()
    print("{} is carrying the following items in inventory: \n".format(hero.name))
    index = 1
    for x in hero.inventory:
        print("{}. {}".format(index, x))
        print()
        index += 1
    print("Type the name of item you would like to use/equip or enter anything to go back: ")
    raw_input = input().lower().strip()
    if raw_input == "super tonic":
        supertonic.heal(hero)
        hero.inventory.remove(supertonic)
    elif raw_input == "helmet":
        if helmet in hero.armor:
            print("{} already is wearing a {}".format(hero.name, helmet.name))
        else:
            helmet.equipped(hero)
            hero.inventory.remove(helmet)
            hero.armor.append(helmet)
    elif raw_input == "chest plate":
        if chestplate in hero.armor:
            print("{} already is wearing a {}".format(hero.name, chestplate.name))
        else:
            chestplate.equipped(hero)
            hero.inventory.remove(chestplate)
            hero.armor.append(chestplate)
    elif raw_input == "gauntlets":
        if gauntlets in hero.armor:
            print("{} already is wearing a {}".format(hero.name, gauntlets.name))
        else:
            gauntlets.equipped(hero)
            hero.inventory.remove(gauntlets)
            hero.armor.append(gauntlets)
    elif raw_input == "leggings":
        if leggings in hero.armor:
            print("{} already is wearing a {}".format(hero.name, leggings.name))
        else:
            leggings.equipped(hero)
            hero.inventory.remove(leggings)
            hero.armor.append(leggings)
    elif raw_input == "evade":
        evade.evadeAttack(hero)
        hero.inventory.remove(evade)
    elif raw_input == "sword":
        if sword in hero.weapon:
            print("{} already is wielding a {} \n".format(hero.name, sword.name))
        else:
            sword.boostAttack(hero)
            hero.inventory.remove(sword)
            hero.weapon.append(sword)
    elif raw_input == "die zombie":
        die.dieZombie(zombie)
        hero.inventory.remove(die)
    else:
        print("Lurn 2 spel dumdum")
    
    
lobby()