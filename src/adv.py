from room import Room
from player import Player
from item import Item, LightSource

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.", True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", False),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", False),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", False),
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

# Give some colors


def print_green(x): print("\033[92m {}\033[00m" .format(x))


def print_purple(x): print("\033[95m {}\033[00m" .format(x))


def print_blue(x): print("\033[96m {}\033[00m" .format(x))


# Items
item = {'lightsaber': Item('lightsaber', 'luminescent blade of magnetically contained plasma'),
        'nuts': Item('nuts', ' fruit composed of an inedible hard shell and a seed, which is generally edible'),
        'gold': Item('gold', 'a box of GOLD NUGGETS'),
        'flashlight': LightSource('flashlight', 'extreme high beam flashlight'),
        'videotape': Item('videotape', 'magnetic tape used for storing video and usually sound in addition.')}

room['outside'].items.append(item['lightsaber'])
room['outside'].items.append(item['flashlight'])
room['foyer'].items.append(item['nuts'])
room['overlook'].items.append(item['gold'])
room['narrow'].items.append(item['videotape'])

last_item = ''

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print_purple(
    '\n############## Welcome to the great adventure game! ################\n'
    .upper())
# new player
user_name = input("Hello there, please enter your name: ")
player = Player(user_name, room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
instructional_text = """
********************** Available Move Options *********************
**** { n } North | { s } South |  { w } West | { e } East ****
************** Enter [q] to Exit the Adventure Game ***************
"""



def main():
    print_welcome_message()
    user = player.name.upper()
    print_blue('Welcome ' + user)
    player.print_current_room()
    input_player_action()


def print_welcome_message():
    # welcome_message = '\n** Welcome to Adventure Game! **'
    
    print_purple(instructional_text)


def input_player_action():
    input_message = '\nWhat would you like to do? [press o to see your options] '
    key = input(input_message).split(' ')
    check_input(key)


def check_input(input):
    if len(input) == 1:
        key = input[0].lower()

        cardinal_directions = {'n': 'North',
                               's': 'South',
                               'e': 'East',
                               'w': 'West'}

        if key == 'q':
            quit_game()
        elif key == 'o':
            print_options()
        elif key == 'l':
            player.print_current_room()
            input_player_action()
        elif key == 'i':
            player.print_inventory()
            input_player_action()
        elif key in cardinal_directions.keys():
            print_green(f'You move {cardinal_directions[key]}.')
            player.move_room(key)
            player.print_current_room()
            input_player_action()
        else:
            bad_input()
    elif len(input) == 2:
        action = input[0].lower()
        obj = input[1].lower()
        global last_item
        if obj == 'it':
            obj = last_item
        last_item = obj

        if action == 'get' or action == 'take':
            player.get(obj)
            input_player_action()
        elif action == 'drop':
            player.drop(obj)
            input_player_action()
        else:
            bad_input()
    else:
        bad_input()


def print_options():
    print_blue('n: go North')
    print_blue('s: go South')
    print_blue('e: go East')
    print_blue('w: go West')
    print_blue('l: check location')
    print_blue('i: check inventory')
    print_blue('get/take [item]: pick up item')
    print_blue('drop [item]: drop item')
    print_blue('q: quit game')
    input_player_action()


def bad_input():
    print("\nYou can't do that in here!")
    input_player_action()


def quit_game():
    print_purple('\nHave a nice day!')


main()