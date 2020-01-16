import textwrap
import random

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

daniel = Player("daniel", "outside")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#

def get_user_choice(): 
    choice = input("[n] north    [s] south   [e] east   [w] west    [q] quit\n")
    return choice_options[choice] # Connected to choice_opions variable below with matching characters

choice_options = {
    "n": "north",
    "s": "south",
    "e": "east",
    "w": "west",
    "q": "quit"
}  

# Give user clear instructions RE: game play

welcome_message = "Hello, Player #1! You are outside. Where to? Choose a direction: North(n), South(s), East(e), or West(w). Press q to Quit."

# Start Game

def show_welcome_message():
    print(welcome_message)

# Connect user input to behavior described in function

user_choice = get_user_choice()

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
