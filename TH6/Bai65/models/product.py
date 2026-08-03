class Product:
    
    def __init__(self, name="", price = 0, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def total(self):
        return self.price * self.quantity