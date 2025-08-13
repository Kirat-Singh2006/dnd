import random
# Banner
from datetime import datetime
from colorama import init, Fore, Style

init()

banner = (
    "\033[38;5;205m"  # Start bright pink
    r"""
  _____                _____        ______  _____   ______         _____    ____   ____ 
 |\    \   _____   ___|\    \   ___|\     \|\    \ |\     \    ___|\    \  |    | |    |
 | |    | /    /| |    |\    \ |     \     \\\    \| \     \  /    /\    \ |    | |    |
 \/     / |    || |    | |    ||     ,_____/|\|    \  \     ||    |  |    ||    |_|    |
 /     /_  \   \/ |    |/____/ |     \--'\_|/ |     \  |    ||    |  |____||    .-.    |
|     // \  \   \ |    |\    \ |     /___/|   |      \ |    ||    |   ____ |    | |    |
|    |/   \ |    ||    | |    ||     \____|\  |    |\ \|    ||    |  |    ||    | |    |
|\ ___/\   \|   /||____| |____||____ '     /| |____||\_____/||\ ___\/    /||____| |____|
| |   | \______/ ||    | |    ||    /_____/ | |    |/ \|   ||| |   /____/ ||    | |    |
 \|___|/\ |    | ||____| |____||____|     | / |____|   |___|/ \|___|    | /|____| |____|
    \(   \|____|/   \(     )/    \( |_____|/    \(       )/     \( |____|/   \(     )/  
     '      )/       '     '      '    )/        '       '       '   )/       '     '
"""
    "\033[0m"  # Reset color
)

print(banner)

print(Fore.WHITE + "\n****************************************************************")
print("*  Copyright of wrench project, 2025                           *")
print(f"*  Loaded at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}                *")
print("****************************************************************" + Style.RESET_ALL)

def roll_dice(sides=20, times=1):
    return [random.randint(1, sides) for _ in range(times)]

class Character:
    def __init__(self, name, hp, strength, dexterity, inventory=None, spells=None):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.strength = strength
        self.dexterity = dexterity
        self.inventory = inventory if inventory else []
        self.spells = spells if spells else []

    def attack(self, target):
        roll = roll_dice()[0]
        damage = roll + self.strength
        target.hp -= damage
        return f"{self.name} attacks {target.name} for {damage} damage!"

    def cast_spell(self, target):
        if not self.spells:
            return f"{self.name} has no spells to cast!"
        spell = random.choice(self.spells)
        damage = roll_dice(6)[0] + self.dexterity
        target.hp -= damage
        return f"{self.name} casts {spell} on {target.name} for {damage} damage!"

    def use_item(self):
        if not self.inventory:
            return f"{self.name} has no items!"
        item = self.inventory.pop(0)
        if item == "Healing Potion":
            heal_amount = random.randint(5, 15)
            self.hp = min(self.max_hp, self.hp + heal_amount)
            return f"{self.name} uses a {item} and heals {heal_amount} HP!"
        return f"{self.name} uses {item}."

    def is_alive(self):
        return self.hp > 0

def create_player():
    name = input("Enter your character's name: ")
    hp = random.randint(20, 30)
    strength = random.randint(1, 5)
    dexterity = random.randint(1, 5)
    inventory = ["Healing Potion", "Healing Potion"]
    spells = ["Fireball", "Magic Missile"]
    return Character(name, hp, strength, dexterity, inventory, spells)

def create_monster():
    name = random.choice(["Goblin", "Orc", "Troll"])
    hp = random.randint(15, 25)
    strength = random.randint(2, 5)
    dexterity = random.randint(1, 4)
    spells = ["Poison Dart", "Shadow Bolt"]
    inventory = ["Healing Potion"]
    return Character(name, hp, strength, dexterity, inventory, spells)

def combat(player, monster):
    print(f"\nA wild {monster.name} appears!")
    while player.is_alive() and monster.is_alive():
        print(f"\n{player.name} HP: {player.hp} | {monster.name} HP: {monster.hp}")
        action = input("Choose an action (attack/spell/item): ").lower()
        if action == "attack":
            print(player.attack(monster))
        elif action == "spell":
            print(player.cast_spell(monster))
        elif action == "item":
            print(player.use_item())
        else:
            print("Invalid action. Turn skipped.")
        
        if not monster.is_alive():
            print(f"{monster.name} is defeated! You win!")
            break

        # Monster turn
        monster_choice = random.choice(["attack", "spell", "item"])
        if monster_choice == "attack":
            print(monster.attack(player))
        elif monster_choice == "spell":
            print(monster.cast_spell(player))
        elif monster_choice == "item":
            print(monster.use_item())

player = create_player()
monster = create_monster()
combat(player, monster)
