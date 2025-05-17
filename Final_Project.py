# Project by Young-Do Krienbuehl for INST326

import requests
##from bs4 import BeautifulSoup
import random


#Global Player State
class Player:
    '''
    
    '''
    def __init__(self):
        self.max_hp = 100
        self.hp = 100
        self.currency = 0
        self.inventory = {}
    
    def add_currency(self, amount):
        self.currency += amount

    def show_currency(self):
        print(f'Currency: {self.currency}')

    def add_item(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
        else:
            self.inventory[item_name] = {'quantity': quantity}
        print(f"{quantity} {item_name}(s) added to inventory.")

    def view_inventory(self):
        if self.inventory:
            print("Current Inventory:")
            for item_name, details in self.inventory.items():
                print(f"- {item_name}: Quantity - {details['quantity']}")
        else:
            print("Inventory is empty.")

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0


player = Player()
goblin = Enemy("Goblin", 30, 7)
dragon = Enemy("Dragon", 100, 15)
golem = Enemy("Golem", 60, 10)
skeleKing = Enemy("Skeleton King", 200, 20)

    
'''        
player = Player()
player.add_currency(10)
player.show_currency()  # => Currency: 10
player.add_item()
inventory = {}
'''
# Example usage
'''
add_item("Laptop", 5)
add_item("Mouse", 10)
view_inventory()
'''


def intro():
    ##print(get_quote())
    print("#############################################")
    print("#                                           #")
    print("#                                           #")
    print("#                                           #")
    print("#           The Call to Adventure           #")
    print("#                                           #")
    print("#                                           #")
    print("#                                           #")
    print("#############################################\n\n\n")
    print("Welcome to Young-Do Krienbuehl's Text Adventure Game!")
    print("You wake up at the entrance of a dark cave. You feel around your pockets for stuff, and find a map, torch, and some gold coins.\n")
    player.add_item("Torch", 1)
    player.add_item("Map", 1)
    player.add_currency(100)
    print("Torch, Map, and 100 Gold Coins added to inventory")
    print("Torch, Map, and 100 Gold Coins added to inventory")
    print("You are at the entrace to a cave. You can either go into the cave or exit and travel north.\n")
    choice = input("").strip().lower()
    if choice == "enter cave":
        cave_interior()
    elif choice == "travel north":
        village()
    else:
        print("That wasn't a valid option. Try again.")

def cave():
    '''
    Serves as player first choice of the game. Whether to go into town or try the cave.
    '''
    choice = input("").strip().lower()
    if choice == "enter cave":
        cave_interior()
    elif choice == "travel north":
        village()
    else:
        print("That wasn't a valid option. Try again.")
    
        

def cave_interior():
    '''
    First Section of cave.
    '''
    print("As you travel into the cave you see a couple of skeletons of other adventures that have activated traps here and died." \
    "")
    print("You encounter a Goblin dude.")
    choice = input("you wanna fight or flee bruh?").strip().lower()
    if choice == "Fight":
        combat(goblin)
    elif choice == "Amulet":
        village()
    else:
        print("That wasn't a valid option. Try again.")
    cave()

def cave_floor2():
    '''
    Deeper section of cave. After this point the player will be traped in the Cave. 
    '''
    print("You go deeper into the cave and encouter a freaking dragon.")
    combat(player, golem)

def cave_final_floor():
    '''
    This is going to be the final floor of the Cave, and contains the final boss.
    '''
    print("This is the final floor of the cave ")
    combat(player, skeleKing)



def village ():
    '''
    Village of Davontry. Gives player oppertunity to buy items and choose next destination.
    '''
    print("You arrive at the village of Davontry. the buildings are made of stone and have a distinct european styling to them.")
    print("You hear children playing in the distance, and then a merchant waves at you.")
    print("The merchant greets you: 'Welcome, traveler! I have potions and weapons for your journey.'")
    choice = input("Do you want the Sword(100)? or Amulet(60)?").strip().lower()
    if choice == "sword":
        player.add_item("Sword", 1)
    elif choice == "amulet":
        player.add_item("Amulet", 1)
    else:
        print("That wasn't a valid option. Try again.")
    print("Cool choice bruh")
    print("You overhear that a Dragon is guarding some treasure.")
    choice_2 = input("Do you want to go to the Forest or back to the Cave?").strip().lower()
    if choice_2 == "forest":
        forest()
    elif choice_2 == "Cave":
        cave()
    else:
        print("That wasn't a valid option. Try again.")

def forest ():
    '''
    Player encouters a dragon and has a chance to get treasure. Player is encouraged to go back to cave.
    '''
    print("You go into the forest and encounter a dragon on your journey")
    combat(player, dragon)
    

def combat(player, enemy):
    '''
    Method for when player engages in combat. Works on a dice based system. 
    If player gets sword, chances to do damage goes up.

    '''
    print(f"\nYou encounter a {enemy.name} with {enemy.health} HP!")

    while enemy.is_alive() and player.hp > 0:
        input("Press Enter to roll the die... 🎲")
        roll = random.randint(1, 6)
        print(f"You rolled a {roll}!")

        if roll in [1, 2]:
            damage = 10
            enemy.health -= damage
            print(f"You hit the {enemy.name} for {damage} damage!")
        else:
            print("You missed!")

        if enemy.is_alive():
            player.hp -= enemy.attack
            print(f"The {enemy.name} hits you for {enemy.attack} damage!")

        print(f"Your HP: {player.hp} | {enemy.name} HP: {enemy.health}\n")

    if player.hp <= 0:
        print("You were defeated.")
    else:
        print(f"You defeated the {enemy.name}!")


def get_quote():

    '''
    
    '''
    try:
        url = "http://quotes.toscrape.com/page/1/"
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        if not quotes:
            return "Welcome, adventurer. The path ahead is yours to forge."

        random_quote = random.choice(quotes)
        text = random_quote.find("span", class_="text").get_text()
        author = random_quote.find("small", class_="author").get_text()

        return f"{text} — {author}"

    except Exception as e:
        return "Welcome, adventurer. The path ahead is yours to forge."

def main_game_loop():
    intro()
if __name__ == "__main__":
    main_game_loop()