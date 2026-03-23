# vấn đề: Cần một dịch vụ để gửi thông báo đến người dùng
# ý tưởng: Tạo một lớp NotificationService để xử lý việc gửi thông báo, 
# cho phép các loại thông báo khác nhau (email, SMS, push notification) có thể được triển khai 
# mà không ảnh hưởng đến mã nguồn chính của hệ thống.
# kết luận: Việc tạo một lớp NotificationService giúp tách biệt logic gửi thông báo khỏi các phần khác của hệ thống, 
# đồng thời cho phép dễ dàng mở rộng và bảo trì mã nguồn trong tương lai.

class NotificationService: 
    def send(self, notification, message): 
        notification.send(message)