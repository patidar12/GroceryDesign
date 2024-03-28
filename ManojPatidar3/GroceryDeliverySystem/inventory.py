from item import Item

class Inventory:
    def __init__(self, item: Item, quantity: int):
        self.item: Item = item
        self.quantity: int = quantity
    