# Use Case Description

## Use Case 1: Đăng nhập hệ thống

| Mục | Mô tả |
|-----|-------|
| **Tên Use Case** | Đăng nhập |
| **Mục tiêu** | Cho phép khách hàng truy cập hệ thống bằng tài khoản hợp lệ |
| **Actor chính** | Khách hàng |
| **Pre-condition** | Khách hàng đã có tài khoản trong hệ thống |
| **Main Flow** | 1. Khách hàng nhập username & password <br> 2. Hệ thống kiểm tra <br> 3. Nếu hợp lệ → vào trang chủ |
| **Alternative Flow** | - Nếu sai username/password → báo lỗi <br> - Nếu quên mật khẩu → chọn chức năng “Quên mật khẩu” |
| **Post-condition** | Khách hàng đăng nhập thành công hoặc nhận thông báo lỗi |

---

## Use Case 2: Đặt hàng

| Mục | Mô tả |
|-----|-------|
| **Tên Use Case** | Đặt hàng |
| **Mục tiêu** | Cho phép khách hàng đặt mua sản phẩm trong giỏ hàng |
| **Actor chính** | Khách hàng |
| **Pre-condition** | Khách hàng đã đăng nhập và giỏ hàng có sản phẩm |
| **Main Flow** | 1. Khách hàng mở giỏ hàng → chọn “Đặt hàng” <br> 2. Hệ thống hiển thị thông tin đơn hàng <br> 3. Khách hàng xác nhận <br> 4. Hệ thống ghi nhận đơn hàng và chuyển sang thanh toán |
| **Alternative Flow** | - Nếu giỏ hàng trống → báo lỗi <br> - Nếu khách hàng hủy → quay lại giỏ hàng |
| **Post-condition** | Đơn hàng được lưu thành công trong hệ thống với trạng thái “Chờ thanh toán” |
