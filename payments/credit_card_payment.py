from payments.payment import Payment 

class CreditCardPayment(Payment): 
    def pay(self, amount): 
        print(f"Processing credit card payment: ${amount}")