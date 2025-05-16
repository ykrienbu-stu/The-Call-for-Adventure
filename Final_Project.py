# Project by Young-Do Krienbuehl

import requests
from bs4 import BeautifulSoup
import random


#Global Player State
class Player:
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

goblin = {"name": "Goblin", "health": 30, "attack": 7}
dragon = {"name": "Goblin", "health": 10, "attack": 15}
golem = {"name": "Goblin", "health": 30, "attack": 5}
skeleKing = {"name": "Skeleton King", "health": 200, "attack": 20}

    
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
    print("#############################################")
    print("#                                           #")
    print("#                                           #")
    print("#                                           #")
    print("#           The Call for Adventure          #")
    print("#                                           #")
    print("#                                           #")
    print("#                                           #")
    print("#############################################\n\n\n")
    print("Welcome to Young-Do Krienbuehl's Text Adventure Game!")
    print("You wake up at the entrance of a dark cave. You feel around your pockets for stuff, and find a map, torch, and some gold coins.\n")
    print("You are at the entrace to a cave. You can either go into the cave or exit and travel north.")
    choice = input("Input (North) or (Enter)")

def cave():
    
    choice = input("")
    if choice == "enter cave":
        cave_interior()
    elif choice == "travel north":
        village()
    else:
        print("That wasn't a valid option. Try again.")
    cave()
        

def cave_interior():
    print("As you travel into the cave you see a couple of skeletons of other adventures that have activated traps here and died." \
    "")
    print("you encounter a fat ass Goblin dude.")
    choice = input("you wanna fight or flee bruh?").strip().lower()
    if choice == "Fight":
        combat(goblin)
    elif choice == "Amulet":
        village()
    else:
        print("That wasn't a valid option. Try again.")
    cave()


def village ():
    print("You arrive at the village of Davontry. the buildings are made of stone and have a distince european styling to them.")
    print("You hear children playing in the distance, and then a merchent waves at you.")
    print("The merchant greets you: 'Welcome, traveler! I have potions and weapons for your journey.'")
    choice = input("Do you want the Sword(100)? or Amulet(60)?")
    if choice == "Sword":
        add_item("Sword", 10)
    elif choice == "Amulet":
        village()
    else:
        print("That wasn't a valid option. Try again.")
    cave()

def forest ():
    print("You go into the forest and encounter a dragon on your journey")
    combat(player, dragon)
    

def combat(player, enemy):
    print(f"\nYou encounter a {enemy['name']} with {enemy['health']} HP!")

    while enemy["health"] > 0 and player.hp > 0:
        input("Press Enter to roll the die... 🎲")
        roll = random.randint(1, 6)
        print(f"You rolled a {roll}!")

        if roll in [1, 2]:
            damage = 10
            enemy["health"] -= damage
            print(f"You hit the {enemy['name']} for {damage} damage!")
        else:
            print("You missed!")

        # Enemy turn (optional)
        if enemy["health"] > 0:
            enemy_damage = enemy["attack"]
            player["health"] -= enemy_damage
            print(f"The {enemy['name']} hits you for {enemy_damage} damage!")
    


def get_quote():
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