class Order: 
    def __init__(self, cart): 
        self.cart = cart 
        self.status = "CREATED" 
        
    def get_total(self): 
        return self.cart.get_total() 
    
    def complete_order(self): 
        self.status = "COMPLETED"