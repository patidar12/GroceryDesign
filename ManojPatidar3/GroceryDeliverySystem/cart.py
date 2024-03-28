from typing import List

from inventory import Inventory

class CartItem:
    def __init__(self, category: str, price: float, quantity: int):
        self.cateogry = category
        self.price = price
        self.quantity = quantity

class Cart:
    def __init__(self):
        self.cart_items : List[CartItem] =  []

    def add_cart(self, inventory: Inventory, quantity):
        if inventory.quantity < quantity:
            raise Exception("Insufficient inventory")
        item = inventory.item
        cart_item = CartItem(item.name, item.price, quantity)
        self.cart_items.append(cart_item)

