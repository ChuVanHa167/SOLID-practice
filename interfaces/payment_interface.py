# vấn đề: Định nghĩa một interface cho hệ thống thanh toán
# ý tưởng: Sử dụng abstract base class để định nghĩa một interface cho hệ thống thanh toán, 
# cho phép các phương thức thanh toán khác nhau có thể được triển khai mà không ảnh hưởng đến mã nguồn chính của hệ thống.
# kết luận: Việc sử dụng abstract base class giúp tạo ra một interface rõ ràng và dễ dàng mở rộng 
# cho hệ thống thanh toán, đồng thời giảm sự phụ thuộc giữa các thành phần của hệ thống.

from abc import ABC, abstractmethod 
class PaymentInterface(ABC): 
    @abstractmethod 
    def pay(self, amount): 
        pass