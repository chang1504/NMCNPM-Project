# ATM Mini-Project – Final Report

## 1. Giới thiệu
ATM Mini-Project là sản phẩm tổng hợp từ các lab trước, mục tiêu:
- Mô phỏng hệ thống rút tiền qua thẻ ATM.
- Tích hợp các thành phần UML, Database, Module, Test, và Quản lý dự án (Jira).
- Trình bày demo: Đăng nhập → Rút tiền → Kiểm thử.

---

## 2. UML Models

### 2.1 Use Case Diagram
![Use Case](artifacts/UseCaseDiagram.pdf)

### 2.2 Sequence Diagram
![Sequence](artifacts/ATM_Withdraw_Sequence.png)

### 2.3 Class Diagram
![Class Diagram](artifacts/Class-atm.png)

---

## 3. Database Design

### 3.1 ERD
![ERD](artifacts/erd.png)

### 3.2 Database Schema
![DB Schema](artifacts/db_schema.png)

---

## 4. Giao diện & Module

### 4.1 Form Login
![Login Form](artifacts/formlogin.png)

### 4.2 Withdraw Module
![Withdraw Demo](artifacts/test_withdraw.png)

---

## 5. Testing

### 5.1 Unit Test (verify_pin, withdraw)
- Case: PIN đúng / PIN sai  
- Case: Đủ tiền / Không đủ tiền

### 5.2 Integration Test (Login Form với Selenium)
- Case: Login thành công  
- Case: Login sai  
- Case: Empty input  

**Kết quả test:**
![Test Report](artifacts/selenium_test_login.png)

---

## 6. Quản lý dự án với Jira
Sprint Planning, Task breakdown, Burndown chart.

### Jira Backlog
![Backlog](artifacts/Jirareport/Screenshot_backlog.png)

### Jira Board
![Board](artifacts/Jirareport/Screenshot_board.png)
![Board 2](artifacts/Jirareport/Screenshot_board2.png)

### Jira Burndown
![Burndown](artifacts/Jirareport/Screenshot_burndown.png)


## 7. Demo cuối kỳ
- Chạy form login (Lab04).  
- Rút tiền từ DB (Lab07).  
- Kết hợp test (Lab08).  
- Trình bày Jira sprint (Lab09).  

**Hình demo:**
![Final Demo](artifacts/final_demo.png)

---

## 8. Kết luận & Định hướng mở rộng
- Hoàn thiện ATM mini-project với các module cơ bản.  
- Kết nối đầy đủ UML → Database → Module → Test → Quản lý.  
- Định hướng mở rộng:
  - Thêm chức năng chuyển khoản, in biên lai.
  - Tích hợp UI web/mobile.
  - Bảo mật nâng cao (hash + salt, OTP).

---

## 9. Tài liệu tham khảo
- Giáo trình môn NMCNPM.  
- MySQL Documentation.  
- PyTest, Selenium Docs.  
- Jira Atlassian Docs.  

---
