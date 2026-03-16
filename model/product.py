class Product: 
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
    
    def display(self):
        print(f"{self.name} - {self.price}")