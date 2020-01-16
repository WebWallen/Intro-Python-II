from room import Room
from player import Player 
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Above syntax required because rooms are defined within big object versus separate variables

# Make a new player object that is currently in the 'outside' room.

player = Player("daniel", room["outside"])

# Define items that can be picked up with a name, category, and description

item = {
    'knife': Item("Knife", "Weapon", "It won't help you in a shoot-out but could provide an unfair advantage in a fist fight."),
    # 'gun': Item("Gun", "Weapon", "The mafia is known to lurk our lands. If you run into them, this gun could save your life!"),
    # 'rubber_chicken': Item("Rubber Chicken", "Weapon", "No other weapons? Throw this and hope it distracts your nemesis."),
    # 'bomb': Item("Bomb", "Weapon", "Trapped in a room full of zombies? Light the fuse and run away as fast as you can."),
    # 'nuke': Item("Nuke", "Weapon", "I don't recommend using this unless your only other option is torture by mafia..."),
    # 'banana': Item("Banana", "Food", "Potassium is known to raise your strength and defenses by 5-10x."),
    # 'coffee': Item("Coffee", "Food", "I don't recommend falling asleep. Drink this to raise energy!"),
    # 'taco': Item("Taco", "Food", "The best nourishment available on the planet... nom to the nom!"),
    # 'liquor': Item("Liquor", "Food", "You might need this to cope with the existence of zombies."),
    'corpse': Item("Corpse", "Food", "Cannibalism is wrong but it's here if you get desperate.")
}

# Add items to specific rooms so they may be accessed by player

room['outside'].items.append(item['knife'])
# room['outside'].items.append(item['rubber_chicken'])
# room['foyer'].items.append(item['knife'])
# room['foyer'].items.append(item['coffee'])
# room['overlook'].items.append(item['gun'])
# room['overlook'].items.append(item['taco'])
# room['narrow'].items.append(item['bomb'])
# room['narrow'].items.append(item['liquor'])
# room['treasure'].items.append(item['nuke'])
room['outside'].items.append(item['corpse'])

def start_game():
    show_welcome_message()
    input_action()

# Welcome displays at beginning of every game

def show_welcome_message():
    welcome_message = "\n** Are You Ready for a Fun Adventure? **\n"
    print(welcome_message)

# Need unique/different message since move_player prints as well

def show_location():
    print('Your current location: ', player.current_room.name)
    print(player.current_room.description, '\n')
    for item in player.current_room.items:
        print(f"Found a {item.category}! It is a {item.name}. \n Description: {item.description}\n")

# Establishes current room

def input_action():
    show_location()
    input_decision()

# Need above logic for fluid gameplay, go from 1 move to the next one

def print_options():
    print('n: move north')
    print('s: move south')
    print('e: move east')
    print('w: move west')
    print('l: check location')
    print('i: check inventory')
    print('take [item]: pick up item')
    print('drop [item]: leave item')
    print('q: quit game')
    input_decision()

def input_decision():
    input_message = '\n Now what? [type o to explore your options]'
    key = input(input_message).split(' ')
    input_options(key)

def wrong_input():
    print("That's not an option. Try again!")
    input_decision()

def input_options(input): 
    if len(input) == 1:
        key = input[0]

        directions = {
            "n": "north",
            "s": "south",
            "e": "east",
            "w": "west",
        }  

        if key == 'q':
            quit_game()
        elif key == 'o':
            print_options()
        elif key == 'l':
            input_action()
        elif key == 'i' or key == 'inventory':
            check_inventory()
            input_decision()
        elif key in directions.keys():
            print(f"You move {directions[key]}\n")
            # Surrounded in {} because it's a dictionary and must match variable sytax
            change_rooms(key)
            input_action()
        else: 
            wrong_input()
    
    elif len(input) == 2:
        if input[0] == 'take':
            get_item(input[1])
        elif input[0] == 'drop':
            drop_item(input[1])
        else:
            wrong_input()
    else: 
        wrong_input()

# Notice player_decision is called whether their choice is valid or not. This function is what gives the player an ability to move either way.

def change_rooms(choice): 
    link_choices = { 'n': 'n_to', 's': 's_to', 'e': 'e_to', 'w': 'w_to'}
    # Connects directions inputted after prompt and directions the game allows you to move
    next_room = getattr(player.current_room, link_choices[choice])

    if not next_room:
        print("Sorry, you can't go that way. Please try again.")
    else:
        player.current_room = next_room

# Check current items

def check_inventory():
    if not len(player.items):
        print('\n No items available.\n')
    else: 
        print('Items available:')
        for item in player.items: 
            print(f'{item.name}\n{item.category}\n{item.description}\n')

# Pick up item

def get_item(item_to_get):
    if any(item.name == item_to_get for item in player.current_room.items):
        player.items.append(item[item_to_get])
        player.current_room.items.remove(item[item_to_get])
        print(f"You're the proud new owner of a {item_to_get}!")
    else:
        print(f"Sorry, there's not a {item_to_get} in here.")
    input_decision()

# Put item back

def drop_item(item_to_drop): 
    if any(item.name == item_to_drop for item in player.items):
        player.items.remove(item[item_to_drop])
        player.current_room.itmes.append(item[item_to_drop])
        print(f"Say goodbye to your {item_to_drop}!")
    else:
        print(f"Oops, you don't even have a {item_to_drop}.")
    input_decision()

# Logic to quit game

def quit_game():
    print("Thanks for playing! Come back soon.\n")

# Nothing happens unless you call function to initialize game settings

start_game()