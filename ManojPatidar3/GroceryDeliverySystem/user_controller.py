from user import User
from inventory_controller import InventoryController

class UserController:

    def __init__(self):
        self.name_vs_user = {}
    
    def get_user_by_name(self, name: str):
        return self.name_vs_user.get(name)
    
    def add_user(self, name: str, address: str, wallet: int):
        user = self.get_user_by_name(name)
        if user:
            raise Exception("User with similar name alrady exists")
        user = User(name, address, wallet)
        self.name_vs_user[name] = user

    def add_to_cart(self, user_name, category: str, brand: str, quantity: int):
        user = self.get_user_by_name(user_name)
        if not user:
            raise Exception("User not present")
        inventories = InventoryController.get_inventory_by_brand_category(brand, category)
        if not inventories:
            raise Exception("No inventory present")
        inventory = inventories[0]
        one_item_price = inventory.item.price
        if one_item_price * quantity > user.wallet:
            raise Exception("Insufficient funds")
        user.cart.add_cart(inventory, quantity)
        inventory.quantity -= quantity
        user.wallet -= (one_item_price * quantity)

    def get_cart(self, user_name: str):
        user = self.get_user_by_name(user_name)
        if not user:
            raise Exception("User not present")
        return user.cart
