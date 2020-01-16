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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("daniel", room["outside"])
# Above syntax required because rooms are defined within big object versus separate variables

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

# Need logic for fluid gameplay, go from 1 move to the next one

def move_player(): 
    choice_options = {
        "n": "north",
        "s": "south",
        "e": "east",
        "w": "west",
        "q": "quit"
    }  

    choice = input("Which direction shall you travel? [n] north    [s] south   [e] east   [w] west    [q] quit\n")

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

def change_rooms(choice): 
    link_choices = { 'n': 'n_to', 's': 's_to', 'e': 'e_to', 'w': 'w_to'}
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