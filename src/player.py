# Write a class to hold player information, e.g. what room they are in
# currently.
from item import LightSource

def print_green(x): print("\033[92m {}\033[00m" .format(x))
def print_purple(x): print("\033[95m {}\033[00m" .format(x))
def print_cyan(x): print("\033[96m {}\033[00m" .format(x))
def print_warning(x): print("\033[93m {} \033[00m" .format(x))
def print_light_purple(x): print("\033[94m {}\033[00m" .format(x))


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
    
    def print_player_name(self):
        print_green(self.name)

    def print_current_room(self):
        if self.current_room.is_light or self.has_light():
            print_light_purple(self.current_room)
            self.current_room.print_items()
        else:
            print('')
            print_light_purple(self.current_room.name)
            print_light_purple("It's pitch black!")

    def print_inventory(self):
        if not len(self.items):
            print_green('\nYour bag is empty.')
        else:
            print_green('\nIn your bag:')
            for item in self.items:
                print_green(item)

    def move_room(self, direction):
        new_room = getattr(self.current_room, f'{direction}_to')
        if not new_room:
            print_warning('\nYou cannot move in that direction!')
        else:
            self.current_room = new_room

    def get(self, item_to_get):
        if self.current_room.is_light or self.has_light():
            if any(item.name == item_to_get for item in self.current_room.items):
                item_obj = next(
                    (item for item in self.current_room.items if item.name == item_to_get), None)
                self.items.append(item_obj)
                self.current_room.items.remove(item_obj)
                item_obj.on_take()
            else:
                print_warning(
                    f"Doesn't look like there's a {item_to_get} in this room...")
        else:
            print_warning('Good luck finding that in the dark!')

    def drop(self, item_to_drop):
        if any(item.name == item_to_drop for item in self.items):
            item_obj = next(
                (item for item in self.items if item.name == item_to_drop), None)
            self.items.remove(item_obj)
            self.current_room.items.append(item_obj)
            item_obj.on_drop()
        else:
            print_green(f"You don't even have a {item_to_drop}!")

    def has_light(self):
        return any(isinstance(item, LightSource) for item in self.items)
    
    def __str__(self):
        return f'\n{self.name} {self.current_room}'