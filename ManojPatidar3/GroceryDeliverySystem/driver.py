from item_controller import ItemController
from inventory_controller import InventoryController
from user_controller import UserController


item_controller =  ItemController()
inventory_controller = InventoryController()
user_controller = UserController()

item_controller.add_item("Amul", "Milk", 100)
item_controller.add_item("Amul", "Curd", 50)
item_controller.add_item("Nestle", "Milk", 60)
item_controller.add_item("Nestle", "Curd", 90)

inventory_controller.add_inventory("Amul", "Milk", 10)
inventory_controller.add_inventory("Nestle", "Milk", 15)
inventory_controller.add_inventory("Amul", "Curd", 10)
inventory_controller.add_inventory("Nestle", "Curd", 5)

print(inventory_controller.search())


user_controller.add_user("Jhonny", "CartoonNetwork", 600)
user_controller.add_user("Naruto", "Anime", 500)
user_controller.add_user("Goku", "Anime", 3000)

user_controller.add_to_cart("Jhonny", "Milk", "Nestle", 5)
#user_controller.add_to_cart("Naruto", "Milk", "Nestle", 12)


# item_controller.update_item("Nestle", "Milk", 5)


# user_controller.get_cart("Goku")