from typing import List

from item import Item

class ItemController:
    def __init__(self):
        self.items: List[Item] = []
    
    def add_item(self, brand: str, category: str, price: float):
        item = self.get_item_by_category_brand(category, brand)
        if item:
            raise Exception("Item already present")
        item = Item(category, brand, price)
        self.items.append(item)
    
    def update_item(self, brand: str, category: str, price: float):
        item = self.get_item_by_category_brand(category, brand)
        if not item:
            raise Exception("Item not present")
        item.price = price

    def get_item_by_category_brand(self, category: str, brand: str) -> Item:
        for item in self.items:
            if item.brand == brand and item.name == category:
                return item
