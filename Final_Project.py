# Project by Young-Do Krienbuehl for INST326

import requests
from bs4 import BeautifulSoup
import random
import sys
import re

#Global Player State
class Player:
    '''
    Represents the player character.

    Attributes:
    - max_hp (int): The maximum health points the player can have.
    - hp (int): The current health of the player.
    - currency (int): Amount of in-game gold the player has.
    - inventory (dict): Dictionary of items the player owns and their quantities.

    Methods:
    - add_currency: Increase the player's gold.
    - subtract_currency: Spend gold if sufficient.
    - show_currency: Print current gold.
    - add_item: Add an item to the inventory.
    - remove_item: Remove an item completely from the inventory.
    - view_inventory: Print inventory contents.
    - use_healing_potion: Use a potion to restore health.
    '''
    def __init__(self):
        self.max_hp = 100
        self.hp = 100
        self.currency = 0
        self.inventory = {}
    
    def add_currency(self, amount):
        self.currency += amount
        print(f"{amount} gold coins added to inventory")

    def subtract_currency(self, amount):
        if self.currency >= amount:
            self.currency -= amount
            print(f"{amount} gold spent.")
            return True
        else:
            print("Not enough gold!")
            return False


    def show_currency(self):
        print(f'Currency: {self.currency}')

    def add_item(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
        else:
            self.inventory[item_name] = {'quantity': quantity}
        print(f"{quantity} {item_name}(s) added to inventory.")

    def view_inventory(self):
        print(f"\nCurrency: {self.currency} Gold")
        if self.inventory:
            print("Current Inventory:")
            for item_name, details in self.inventory.items():
                print(f"- {item_name}: Quantity - {details['quantity']}")
        else:
            print("Inventory is empty.\n")

    def use_healing_potion(self):

        if "Healing Potion" in self.inventory and self.inventory["Healing Potion"]["quantity"] > 0:
            self.hp = min(self.max_hp, self.hp + 50)
            self.inventory["Healing Potion"]["quantity"] -= 1
            print("You used a Healing Potion! +50 HP.")
            print(f"Your HP is now {self.hp}/{self.max_hp}")
        else:
            print("You don't have any Healing Potions!")


class Enemy:
    '''
    Represents an enemy in the game with a name, health, and attack power.
    '''
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

## Initialize global player and enemy instances used throughout the game.
player = Player()
# Defines enemies with names, HP health points, and attack values.
goblin = Enemy("Goblin", 30, 7)
dragon = Enemy("Dragon", 100, 15)
golem = Enemy("Golem", 60, 10)
skeleKing = Enemy("Skeleton King", 200, 20)

def quit_game():
    '''
    Function that allows player to quit the game at any point and exits program.
    '''
    print("Thanks for playing! Goodbye, adventurer.")
    sys.exit() 

def get_player_input(prompt):
    """
    Handles player input and checks for 'inventory' keyword.
    """
    while True:
        choice = input(prompt).strip().lower()
        if choice == "inventory" or choice == "i":
            player.view_inventory()
        elif choice == "quit" or choice == "q":
            quit_game()
        else:
            return choice
        

def intro():
    '''
    Serves as intro to the games, and introduces player game commands.
    '''
    print(f"\n\n",get_quote(),"\n\n")
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
    print("You wake up at the entrance of a dark cave. You feel around your pockets for anything useful, and find a map, torch, healing potion, and some gold coins.\n")
    player.add_item("Torch", 1)
    player.add_item("Map", 1)
    player.add_item("Healing Potion", 1)
    player.add_currency(100)
    
    print("You can check your inventory by typing 'inventory' or  'i'. ")
    print("You can also quit the game by typing 'quit' or 'q'. \n")
    print("You are at the entrace to a cave. You can either go into the cave or exit and travel north into town.\n")
    choice = get_player_input("Enter [Cave] or [North]:").strip().lower()
    if choice == "cave":
        cave_interior()
    elif choice == "north":
        village()
    else:
        print("That wasn't a valid option. Try again.")

    
def cave_interior():
    '''
    First Section of cave.
    Player may fight the goblin, flee, or go back to town before engaging.
    '''
    print("You enter the cave and see skeletons of fallen adventurers.")
    print("A Goblin blocks your path.")
    choice = get_player_input("Do you want to [fight] or [flee]?: ").strip().lower()
    if choice == "fight":
        if combat(player, goblin):
            print("You found a Healing Potion and Shield on the Goblin!")
            player.add_item("Healing Potion", 1)
            player.add_item("Shield", 1)

        while True:
            next_step = get_player_input("Do you want to [continue] deeper or [leave] the cave?: ").strip().lower()
            if next_step == "continue":
                cave_floor2()
                break
            elif next_step == "leave":
                print("You decide to leave the cave go to the village.")
                village()
                break
            else:
                print("Invalid choice. Please type 'continue' or 'leave'.")
        else: 
            print("GAME OVER.")
    elif choice == "flee":
        print("You flee like a bitch and instead go to the village\n")
        village()
    else:
        print("That wasn't a valid option. Try again.")
    



def cave_floor2():
    '''
    Deeper section of cave. After this point the player will be traped in the Cave. 
    '''
    print("As you go deeper into the cave, the ground shakes and the hallway behind you collaspes.")
    print("You are unable to turn back, the only way out is forward.")
    print("A statue in front of you comes to life and starts to attack you.")
    if combat(player, golem):
        print("You found a Healing Potion on the Golem!")
        player.add_item("Healing Potion", 1)
        cave_final_floor()
    else:
        print("GAME OVER")



def cave_final_floor():
    '''
    This is going to be the final floor of the Cave, and contains the final boss.
    '''
    print("This is the final floor of the cave. The Skeleton King awaits.")
    if combat(player, skeleKing):
        print("You stand before a glowing chest sealed by ancient magic.")
        print("To open it, you must speak the magic phrase that begins with 'open' and ends with 'please'.")

        while True:
            incantation = get_player_input("Speak the phrase: ")

            # Added this to satisfy Regular expressions requirement.
            if re.match(r"^open.*please$", incantation.strip().lower()):
                print("The magic recognizes your words. The chest opens...")
                print("You obtained the Skeleton Crown! You win!")
                player.add_item("Skeleton Crown", 1)
                break
            else:
                print("Nothing happens. Try again.")
    else:
        print("GAME OVER")



def village():
    '''
    Allows the player to interact with the village.
    Includes merchant access and next location choice.
    '''
    print("You arrive at the village of Davontry.")
    merchant()  # Access merchant store
    print("The Merchant tells you that a Dragon is guarding some treasure in a nearby forest.")

    while True:
        next_choice = get_player_input("Do you want to go to the [Forest] or back to the [Cave]? ").strip().lower()
        if next_choice == "forest":
            forest()
            break
        elif next_choice == "cave":
            cave_interior()
            break
        else:
            print("That wasn't a valid option. Try again.")



def forest():
    '''
    Player encounters a dragon and has a chance to get treasure.
    Afterward, player chooses to go back to the town or cave.
    '''
    print("You go into the forest and encounter a Dragon on your journey.")

    if combat(player, dragon):
        print("You found a set of Armour and 200 Gold!")
        player.add_item("Armour", 1)
        player.add_currency(200)

        # Choice after winning
        while True:
            next_move = get_player_input("Do you want to go back to the [Village] or return to the [Cave]? ").strip().lower()
            if next_move == "village":
                village()
                break
            elif next_move == "cave":
                cave_interior()
                break
            else:
                print("That wasn't a valid option. Please type [Village] or [Cave].")
    else:
        print("GAME OVER")


def get_quote():
    '''
    Handles player input with support for global commands like checking inventory or quitting the game.
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


def combat(player, enemy):
    """
    Handles combat and returns True if player wins, False if they die.
    Combat is dice-based.
    Item effects:
        - Sword: +5 player damage and improved hit chance (1-4 hits instead of 1-2)
        - Amulet: -5 enemy attack and improved hit chance (player hits on 5 instead of just 1-2)
        - Armour: -15 enemy attack 
        - Shield: -15 enemy attack
    """
    print(f"\nYou encounter a {enemy.name} with {enemy.health} HP!")

    # Initialize defaults
    bonus_damage = 0
    damage_reduction = 0
    hit_range = [1, 2]

    # Stackable effects
    if "Sword" in player.inventory:
        bonus_damage += 5
        hit_range += [3, 4]

    if "Amulet" in player.inventory:
        damage_reduction += 5
        hit_range += [5]

    if "Shield" in player.inventory:
        damage_reduction += 15

    if "Armour" in player.inventory:
        damage_reduction += 15
    
    # Remove duplicates and sort hit_range
    hit_range = sorted(list(set(hit_range)))

    while enemy.is_alive() and player.hp > 0:
        action = get_player_input("Type 'roll' or 'r' to fight. Type 'potion' or 'p' to heal: ").strip().lower()
        if action == "potion" or action == 'p':
            player.use_healing_potion()
            continue

        roll = random.randint(1, 6)
        print(f"You rolled a {roll}!")

        if roll in hit_range:
            damage = 10 + bonus_damage
            enemy.health -= damage
            print(f"You hit the {enemy.name} for {damage} damage!")
        else:
            print("You missed!")

        if enemy.is_alive():
            actual_attack = max(enemy.attack - damage_reduction, 0)
            player.hp -= actual_attack
            print(f"The {enemy.name} hits you for {actual_attack} damage!")

        print(f"Your HP: {player.hp} | {enemy.name} HP: {enemy.health}\n")

    if player.hp <= 0:
        print("You were defeated.")
        return False
    else:
        print(f"You defeated the {enemy.name}!")
        return True


def merchant():
    '''
    Allows the player to buy items from the merchant.
    Prevents repurchasing unique items like Sword and Amulet.
    '''
    print("The merchant greets you: 'Welcome, traveler! I have potions and weapons for your journey.'")
    while True:
        choice = get_player_input("Do you want the [Sword]($100), [Amulet]($60), or Healing [Potion]($20)? Type 'done' to finish shopping: ").strip().lower()

        if choice == "sword":
            if "Sword" in player.inventory:
                print("You already own a Sword.")
            elif player.subtract_currency(100):
                player.add_item("Sword", 1)
                print("Merchant: 'Very good choice adventurer'.")

        elif choice == "amulet":
            if "Amulet" in player.inventory:
                print("You already own an Amulet.")
            elif player.subtract_currency(60):
                player.add_item("Amulet", 1)
                print("Merchant: 'May the spirits protect you.'")

        elif choice == "potion":
            if player.subtract_currency(20):
                player.add_item("Healing Potion", 1)
                print("Merchant: 'This will serve you well.'")

        elif choice == "done":
            break

        else:
            print("That wasn't a valid option. Try again.")



def main_game_loop():
    '''
    Starts game and initiates intro sequence.
    '''
    intro()

if __name__ == "__main__":
    main_game_loop()

