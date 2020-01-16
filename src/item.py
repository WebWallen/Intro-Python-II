class Item:
    def __init__(self, name, category, description):
        self.name = name
        self.category = category
        self.description = description

    def take(self):
        print(f"You picked up {self.name}.")

    def drop(self):
        print(f"You dropped {self.name}.")