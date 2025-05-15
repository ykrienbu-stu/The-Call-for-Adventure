
# Project by Young-Do Krienbuehl

#Global Player State
class Player:
    def __init__(self):
        self.max_hp = 100
        self.hp = 100
        self.currency = 0
    
    def add_currency(self, amount):
        self.currency += amount

    def show_currency(self):
        print(f'Currency: {self.currency}')
    




player = Player()
player.add_currency(10)
player.show_currency()  # => Currency: 10

inventory = {}

def add_item(item_name, quantity, price):
    if item_name in inventory:
        inventory[item_name]['quantity'] += quantity
    else:
        inventory[item_name] = {'quantity': quantity, 'price': price}
    print(f"{quantity} {item_name}(s) added to inventory.")

def remove_item(item_name, quantity):
    if item_name in inventory:
        if inventory[item_name]['quantity'] >= quantity:
            inventory[item_name]['quantity'] -= quantity
            print(f"{quantity} {item_name}(s) removed from inventory.")
            if inventory[item_name]['quantity'] == 0:
                del inventory[item_name]
                print(f"{item_name} removed from inventory as quantity is 0.")
        else:
             print(f"Not enough {item_name}(s) in inventory.")
    else:
        print(f"{item_name} not found in inventory.")

# Example usage
'''
add_item("Laptop", 5, 1200)
add_item("Mouse", 10, 25)
view_inventory()
remove_item("Laptop", 2)
update_price("Mouse", 30)
view_inventory()
remove_item("Keyboard", 5)
remove_item("Mouse",10)
view_inventory()
'''
def view_inventory():
    if inventory:
        print("Current Inventory:")
        for item_name, details in inventory.items():
            print(f"- {item_name}: Quantity - {details['quantity']}, Price - ${details['price']}")
    else:
        print("Inventory is empty.")


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
    choice = input("Choose 'deeper' or 'back': ").strip().lower()


def village ():
    print("You arrive at the village of Davontry. the buildings are made of stone and have a distince european styling to them.")
    print("You hear children playing in the distance, and then a merchent waves at you.")

    choice = input("You see a merchant ")




def merchant():
    print("The merchant greets you: 'Welcome, traveler! I have potions and weapons for your journey.'")
    print("But you have no gold. Maybe next time...")


def main_game_loop():
    intro()
if __name__ == "__main__":
    main_game_loop()