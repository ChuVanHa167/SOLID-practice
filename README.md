# SOLID-practice
thực hành SOLID

# Thực Hành SOLID với Python

## Refactor Hệ Thống Order E-Commerce 
(OOP Practice)
```
https://github.com/ChuVanHa167/OOP-Practice
```
---

# 1. Giới thiệu

Repository này là **phần 2 trong chuỗi thực hành Software Design**:

1. OOP Practice
2. SOLID Practice
3. Design Pattern Practice
4. Architecture Integration

Trong repo này, bạn sẽ **refactor hệ thống đã xây ở repo1(OOP Practice)** để áp dụng **5 nguyên tắc SOLID**.

---

# 2. Mục tiêu học tập

Sau khi hoàn thành repo này bạn sẽ:

* Hiểu rõ **5 nguyên tắc SOLID**
* Nhận diện **thiết kế OOP chưa tốt**
* Refactor code để:

  * dễ mở rộng
  * dễ bảo trì
  * giảm coupling

---

# 3. SOLID là gì

SOLID là 5 nguyên tắc thiết kế giúp code:

```
dễ mở rộng
dễ bảo trì
dễ test
```

SOLID gồm:

```
S - Single Responsibility Principle
O - Open Closed Principle
L - Liskov Substitution Principle
I - Interface Segregation Principle
D - Dependency Inversion Principle
```

---

# 4. Bài toán

Tiếp tục phát triển **hệ thống order e-commerce**.

Nhưng lần này hệ thống cần hỗ trợ thêm:

```
nhiều loại payment
nhiều loại notification
nhiều cách lưu dữ liệu
```

Nếu thiết kế không tốt, code sẽ trở nên:

```
khó mở rộng
khó bảo trì
phải sửa code cũ liên tục
```

SOLID giúp giải quyết vấn đề này.

---

# 5. Cấu trúc project

Tạo repo mới:

```
repo2-solid-order-system
```

Cấu trúc:

```
src

models
    product.py
    cart.py
    cart_item.py
    order.py

interfaces
    payment_interface.py
    notification_interface.py

payments
    credit_card_payment.py
    paypal_payment.py

notifications
    email_notification.py
    sms_notification.py

services
    order_service.py

main.py
```

---

# 6. Single Responsibility Principle

## Nguyên tắc

Một class **chỉ nên có một lý do để thay đổi**.

---

## Ví dụ sai

Trong repo1:

```
OrderService
    tạo order
    thanh toán
    gửi email
```

Class này có **3 trách nhiệm**.

---

## Refactor

Tách thành:

```
OrderService
PaymentService
NotificationService
```

---

## Thực hành

Tạo file:

```
services/payment_service.py
```

```python
class PaymentService:

    def process_payment(self, payment, amount):
        payment.pay(amount)
```

---

Tạo file:

```
services/notification_service.py
```

```python
class NotificationService:

    def send(self, notification, message):
        notification.send(message)
```

---

# 7. Open Closed Principle

## Nguyên tắc

Code phải:

```
open for extension
closed for modification
```

Có nghĩa là:

```
muốn thêm tính năng
không cần sửa code cũ
```

---

## Áp dụng

Tạo interface payment.

```
interfaces/payment_interface.py
```

```python
from abc import ABC, abstractmethod

class PaymentInterface(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

---

Các payment method sẽ kế thừa interface này.

```
CreditCardPayment
PaypalPayment
```

Nếu muốn thêm:

```
CryptoPayment
ApplePay
```

Chỉ cần tạo class mới.

---

# 8. Liskov Substitution Principle

## Nguyên tắc

Class con phải có thể **thay thế class cha mà không phá hệ thống**.

Ví dụ:

```
payment = CreditCardPayment()
payment = PaypalPayment()
```

Cả hai đều phải chạy đúng với:

```
payment.pay(amount)
```

---

# 9. Interface Segregation Principle

## Nguyên tắc

Không nên tạo interface quá lớn.

Ví dụ sai:

```
PaymentSystem
    pay()
    refund()
    generate_invoice()
```

Một số class có thể **không cần refund**.

---

## Refactor

Tách interface:

```
PaymentInterface
RefundInterface
```

---

# 10. Dependency Inversion Principle

## Nguyên tắc

Module cấp cao **không phụ thuộc module cấp thấp**.

Cả hai nên phụ thuộc **abstraction**.

---

## Ví dụ sai

```
OrderService
    sử dụng trực tiếp CreditCardPayment
```

---

## Refactor

```
OrderService
    sử dụng PaymentInterface
```

---

## Thực hành

File:

```
services/order_service.py
```

```python
class OrderService:

    def __init__(self, payment_service):
        self.payment_service = payment_service

    def checkout(self, order, payment):

        total = order.get_total()

        self.payment_service.process_payment(payment, total)

        order.complete_order()
```

---

# 11. Demo chương trình

File:

```
main.py
```

```python
from models.product import Product
from models.cart import Cart
from models.cart_item import CartItem
from models.order import Order

from payments.credit_card_payment import CreditCardPayment

from services.order_service import OrderService
from services.payment_service import PaymentService


product = Product(1,"Laptop",1000)

cart = Cart()

cart.add_item(CartItem(product,1))

order = Order(cart)

payment = CreditCardPayment()

payment_service = PaymentService()

order_service = OrderService(payment_service)

order_service.checkout(order,payment)
```

---

# 12. SOLID đã được áp dụng

Single Responsibility

```
OrderService
PaymentService
NotificationService
```

Open Closed

```
PaymentInterface
```

Liskov Substitution

```
CreditCardPayment
PaypalPayment
```

Interface Segregation

```
PaymentInterface
NotificationInterface
```

Dependency Inversion

```
OrderService → PaymentInterface
```

---

# 13. Những lỗi phổ biến

Không nên:

```
tạo quá nhiều interface
áp dụng SOLID cho hệ thống quá nhỏ
```

---

# 14. Sau khi hoàn thành repo này

Bạn sẽ tiếp tục:

```
repo3-design-pattern-order-system
```

Ở repo này chúng ta sẽ áp dụng các **Design Pattern thực tế**:

```
Factory
Strategy
Observer
Singleton
Adapter
```
