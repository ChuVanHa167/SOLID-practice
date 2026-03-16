class OrderService: 
    def __init__(self, payment_service): 
        self.payment_service = payment_service 
        
        def checkout(self, order, payment): 
            total = order.get_total() 
            self.payment_service.process_payment(payment, total) 
            order.complete_order()