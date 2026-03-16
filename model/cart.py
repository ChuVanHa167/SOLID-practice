class Cart: 
    def __init__(self): 
        self.items = [] 
        
    def add_item(self, cart_item): 
        self.items.append(cart_item) 
        
    def get_total(self): 
        total = 0 
        for item in self.items: 
            total += item.get_total() 
            return total