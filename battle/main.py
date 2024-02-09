from classes.Game import Person, bcolors
from classes.Magic import Spell

#create black magic
fire = Spell("fire", 10, 100, "black")
Thunder = Spell("Thunder", 10, 100, "black")
Blizzard = Spell("Blizzard", 10, 100, "black")
Meteor = Spell("Meteor", 20, 200, "black")
Quake = Spell("Quake", 14, 140, "black")

#create white magic
Cure = Spell("Cure", 12, 120, "white")
Cura = Spell("Cura", 18, 200, "white")

#Instantiate people
player = Person(460, 65, 60, 34, [fire, Thunder, Blizzard, Meteor, Quake, Cure, Cura])
enemy = Person(1200, 65, 45, 25, [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "An Enemy Attacks!" + bcolors.ENDC)

while running:
        #choose actions
    print("==================")
    player.choose_action()
    choice = input("choose Action")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("you attacked for", dmg, "points of damage.  Enemy HP:", enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("choose magic:")) - 1

        Spell = player.magic[magic_choice]
        print(Spell.generate_damage())
        magic_dmg = Spell.generate_damage()

        current_mp = player.get_mp()

        if Spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough mp\n" + bcolors.ENDC)
            continue

        player.reduce_mp(Spell.cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + Spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy Attacks for", enemy_dmg)

    print("====================")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    print("your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)

#end of game results
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you")
        running = False


