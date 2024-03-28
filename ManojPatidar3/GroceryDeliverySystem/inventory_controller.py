from typing import List

from inventory import Inventory
from item_controller import ItemController

class InventoryController:
    def __init__(self):
        self.inventories: List[Inventory] = []
        self.item_controller = ItemController()
    
    def add_inventory(self, category: str, brand: str, quantity: int):
        item = self.item_controller.get_item_by_category_brand(category, brand)
        if not item:
            raise Exception("Item not present")
        inventory = Inventory(item, quantity)
        self.inventories.append(inventory)
    

    def get_inventory_by_brand_category(self, brand, category):
        for inventory in self.inventories:
            if inventory.item.brand == brand and inventory.item.name in category:
                return inventory

    def search(self, brands: List[str] = [], categories: List[str] = []) -> List[Inventory]:
        inventories = []
        for inventory in self.inventories:
            if inventory.quantity > 0:
                if brands and categories:
                    if inventory.item.brand in brands and inventory.item.name in categories:
                        inventories.append(inventory)
                elif brands:
                    if inventory.item.brand in brands:
                        inventories.append(inventory)
                elif categories:
                    if inventory.item.name in categories:
                        inventories.append(inventory)
                else:
                    inventories.append(inventory)
        
        return inventories
