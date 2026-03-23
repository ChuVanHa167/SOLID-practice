# vấn đề: Cần một dịch vụ để xử lý các đơn hàng, bao gồm việc thanh toán và hoàn tất đơn hàng
# ý tưởng: Tạo một lớp OrderService để xử lý các đơn hàng, 
# sử dụng một dịch vụ thanh toán để xử lý việc thanh toán và hoàn tất đơn hàng sau khi thanh toán thành công.
# kết luận: Việc tạo một lớp OrderService giúp tách biệt logic xử lý đơn hàng khỏi các phần khác của hệ thống, 
# đồng thời cho phép dễ dàng mở rộng và bảo trì mã nguồn trong tương lai.

class OrderService: 
    def __init__(self, payment_service): 
        self.payment_service = payment_service 
        
    def checkout(self, order, payment): 
        total = order.get_total() 
        self.payment_service.process_payment(payment, total) 
        order.complete_order()