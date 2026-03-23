# vấn đề: Cần một dịch vụ để xử lý các thanh toán, bao gồm việc thực hiện thanh toán 
# và quản lý các phương thức thanh toán khác nhau
# ý tưởng: Tạo một lớp PaymentService để xử lý các thanh toán, 
# cho phép các phương thức thanh toán khác nhau (thẻ tín dụng, PayPal, chuyển khoản ngân hàng) có thể được triển khai 
# mà không ảnh hưởng đến mã nguồn chính của hệ thống.
# kết luận: Việc tạo một lớp PaymentService giúp tách biệt logic xử lý thanh toán khỏi các phần khác của hệ thống, 
# đồng thời cho phép dễ dàng mở rộng và bảo trì mã nguồn trong tương lai.

class PaymentService: 
    def process_payment(self, payment, amount): 
        payment.pay(amount)