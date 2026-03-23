from model.product import Product 
from model.cart import Cart 
from model.cart_item import CartItem 
from model.order import Order 
from payments.credit_card_payment import CreditCardPayment 
from services.order_service import OrderService 
from services.payment_service import PaymentService 

product = Product(1,"Laptop",1000) 
cart = Cart() 
cart.add_item(CartItem(product,)) 
order = Order(cart) 
payment = CreditCardPayment() # tạo một phương thức thanh toán cụ thể (thẻ tín dụng)
payment_service = PaymentService() # tạo một dịch vụ thanh toán để xử lý việc thanh toán
order_service = OrderService(payment_service) # tạo một dịch vụ đơn hàng để xử lý việc thanh toán và hoàn tất đơn hàng
order_service.checkout(order,payment) # thực hiện thanh toán và hoàn tất đơn hàng