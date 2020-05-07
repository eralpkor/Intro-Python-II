def print_green(x): print("\033[92m {}\033[00m" .format(x))
def print_warning(x): print("\033[93m {} \033[00m" .format(x))


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}: {self.description}'

    def on_take(self):
        print_green(f'\nYou have picked up {self.name}!')

    def on_drop(self):
        print_green(f'\nYou have dropped the {self.name}!')


class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def on_drop(self):
        print_warning(
                    f"\nYou have dropped the {self.name}. It's not wise to drop your source of light!")

class Treasure(Item):
    def __init__(self, name, description):
        super().__init__(name, description)