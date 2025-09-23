# ATM Withdraw - Use Case & Sequence Diagram Description

## 1. Use Case Description – Rút tiền

**Tên Use Case:** Rút tiền (Withdraw Cash)  
**Mục tiêu:** Cho phép khách hàng rút tiền mặt từ tài khoản thông qua ATM.  
**Actor chính:** Khách hàng  
**Tác nhân phụ:** Ngân hàng (Bank Server)  
**Điều kiện tiên quyết:**  
- Khách hàng có thẻ ATM và số dư khả dụng.  

**Luồng sự kiện chính:**  
1. Khách hàng đưa thẻ vào ATM.  
2. Hệ thống yêu cầu nhập mã PIN.  
3. Khách hàng nhập PIN.  
4. ATM gửi thông tin xác thực tới Bank Server.  
5. Bank Server kiểm tra PIN và trả kết quả.  
6. Khách hàng chọn giao dịch rút tiền và nhập số tiền.  
7. ATM gửi yêu cầu kiểm tra số dư tới Bank Server.  
8. Bank Server xác nhận số dư hợp lệ.  
9. ATM nhả tiền cho khách hàng.  
10. ATM in biên lai (nếu khách hàng chọn).  
11. ATM trả thẻ.  

**Luồng thay thế:**  
- PIN sai → ATM báo lỗi và yêu cầu nhập lại.  
- PIN sai 3 lần → ATM giữ thẻ.  
- Số dư không đủ → ATM thông báo lỗi, không thực hiện rút tiền.  

**Điều kiện kết thúc:**  
- Khách hàng nhận được tiền và thẻ, hoặc nhận thông báo lỗi.  

---

## 2. Sequence Diagram Description – Rút tiền

### Các đối tượng tham gia
- **Customer:** Người trực tiếp thao tác (đưa thẻ, nhập PIN, chọn số tiền, nhận tiền).  
- **ATM Machine:** Giao diện và xử lý chính của máy ATM (đọc thẻ, xác thực, giao tiếp với server, nhả tiền).  
- **Bank Server:** Hệ thống ngân hàng, có chức năng xác thực PIN, kiểm tra số dư và phản hồi cho ATM.  

### Các thông điệp trao đổi
1. **Customer → ATM:** Insert Card → bắt đầu giao dịch.  
2. **ATM → Customer:** Prompt PIN → yêu cầu nhập mã PIN.  
3. **Customer → ATM:** Enter PIN → nhập mã PIN.  
4. **ATM → Bank Server:** Verify PIN → gửi yêu cầu xác thực.  
5. **Bank Server → ATM:** Return Result → xác thực thành công/thất bại.  
6. **Customer → ATM:** Select Withdraw & Enter Amount → nhập số tiền cần rút.  
7. **ATM → Bank Server:** Check Balance → kiểm tra số dư.  
8. **Bank Server → ATM:** Balance Result → phản hồi đủ/không đủ số dư.  
9. **ATM → Customer:** Dispense Cash → nhả tiền cho khách hàng.  
10. **ATM → Customer:** Print Receipt (optional) → in biên lai nếu khách hàng chọn.  
11. **ATM → Customer:** Eject Card → trả thẻ kết thúc giao dịch.  

---

## 3. Tệp cần nộp lên GitHub
- **ATM_Withdraw_UseCase.png** – Sơ đồ Use Case  
- **ATM_Withdraw_Sequence.png** – Sơ đồ Sequence  
- **ATM_Withdraw_Description.md** – File mô tả chi tiết  
