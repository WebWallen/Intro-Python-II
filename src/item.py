class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def take(self):
        print(f"You picked up {self.name}.")

    def drop(self):
        print(f"You dropped {self.name}.")