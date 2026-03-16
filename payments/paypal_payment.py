from payments.payment import Payment 
class PaypalPayment(Payment): 
    def pay(self, amount): 
        print(f"Processing PayPal payment: ${amount}")