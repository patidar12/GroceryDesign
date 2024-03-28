from cart import Cart

class User:
    def __init__(self, name: str, address: str, wallet: float):
        self.name = name
        self.address = address
        self.wallet = wallet
        self.cart = Cart()
    
    