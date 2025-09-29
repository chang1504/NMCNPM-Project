# Lab 06 – Thiết kế chi tiết lớp & kiến trúc ATM

## 1. Class Diagram
- **ATM**: lớp trung tâm, quản lý các chức năng authenticate, withdraw, deposit, transfer.
- **Card**: chứa thông tin thẻ, trạng thái, PIN hash.
- **Account**: chứa số tài khoản, số dư, có thể debit (trừ tiền) hoặc credit (cộng tiền).
- **Transaction**: lưu thông tin giao dịch, loại, số tiền, thời gian, trạng thái.

Quan hệ:
- ATM liên kết với Card và Transaction.
- Card liên kết với Account.
- Account liên kết với Transaction.

## 2. Package Diagram
- **UI**: giao diện người dùng (LoginForm, WithdrawForm).
- **Controller**: điều khiển luồng xử lý (ATMController).
- **BankService**: dịch vụ nghiệp vụ (AccountService, TransactionService).
- **Hardware**: phần cứng tương tác (CardReader, CashDispenser, Printer).

Luồng chính:
UI → Controller → BankService/Hardware → phản hồi về UI.

## 3. Ghi chú
- Xuất file `.png` từ PlantUML online hoặc VS Code.
- Nộp: `Class-atm.puml`, `Class-atm.png`, `Package-diagram.puml`, `Package-diagram.png`, `notes.md`.
