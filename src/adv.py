import textwrap
import random
import sys

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

knife = Item("Knife", "Weapon", "It won't help you in a shoot-out but could provide an unfair advantage in a fist fight.")
gun = Item("Gun", "Weapon", "The mafia is known to lurk our lands. If you run into them, this gun could save your life!")
rubber_chicken = Item("Rubber Chicken", "Weapon", "No other weapons? Throw this and hope it distracts your nemesis.")
bomb = Item("Bomb", "Weapon", "Trapped in a room full of zombies? Light the fuse and run away as fast as you can.")
nuke = Item("Nuke", "Weapon", "I don't recommend using this unless your only other option is torture by mafia...")
banana = Item("Banana", "Food", "Potassium is known to raise your strength and defenses by 5-10x.")
coffee = Item("Coffee", "Food", "I don't recommend falling asleep. Drink this to raise energy!")
taco = Item("Taco", "Food", "The best nourishment available on the planet... nom to the nom!")
liquor = Item("Liquor", "Food", "You might need this to cope with the existence of zombies.")
corpse = Item("Corpse", "Food", "Cannibalism is wrong but it's here if you get desperate.")

# Add items to specific rooms so they may be accessed by player

room['outside'].items.append(banana, rubber_chicken)
room['foyer'].items.append(knife, coffee)
room['overlook'].items.append(gun, taco)
room['narrow'].items.append(bomb, liquor)
room['treasure'].items.append(nuke, corpse)

def start_game():
    show_welcome_message()
    move_player()

# Welcome displays at beginning of every game

def show_welcome_message():
    welcome_message = "\n** Are You Ready for a Fun Adventure? **\n"
    print(welcome_message)

# Need unique/different message since move_player prints as well

def show_location():
    print('Your current location: ', player.current_room.name)
    print(player.current_room.description, '\n')

# Establishes current room

def player_decision():
    show_location()
    move_player()

# Need above logic for fluid gameplay, go from 1 move to the next one

def move_player(): 
    choice_options = {
        "n": "north",
        "s": "south",
        "e": "east",
        "w": "west",
        "i": "inventory",
        "c": "check",
        "q": "quit"
    }  

    choice = input("Which direction shall you travel? [n] north    [s] south   [e] east   [w] west    [q] quit\n Looking for items? Inspect your inventory with [i] or check the room for food and weapons with [c].")

    if choice == 'q':
        quit_game()
    elif choice in choice_options.keys():
        print(f"You move {choice_options[choice]}\n")
        # Surrounded in {} because it's a dictionary and must match variable sytax
        change_rooms(choice)
        player_decision()
    else: 
        print("That's not a valid choice. Please try again.")
        player_decision()

# Notice player_decision is called whether their choice is valid or not. This function is what gives the player an ability to move either way.

def change_rooms(choice): 
    link_choices = { 'n': 'n_to', 's': 's_to', 'e': 'e_to', 'w': 'w_to'}
    # Connects directions inputted after prompt and directions the game allows you to move
    next_room = getattr(player.current_room, link_choices[choice])

    if not next_room:
        print("Sorry, you can't go that way. Please try again.")
    else:
        player.current_room = next_room

# Logic to quit game

def quit_game():
    print("Thanks for playing! Come back soon.\n")
    sys.exit()

# Nothing happens unless you call function to initialize game settings

start_game()