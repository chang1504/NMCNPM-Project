import mysql.connector
import hashlib

# Hàm kiểm tra PIN
def verify_pin(card_no, pin):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Trang15042005",   # thay bằng mật khẩu MySQL thật của bạn
        database="atm_demo"
    )
    cur = conn.cursor()
    cur.execute("SELECT pin_hash FROM cards WHERE card_no=%s", (card_no,))
    row = cur.fetchone()
    conn.close()
    return row and row[0] == hashlib.sha256(pin.encode()).hexdigest()

# Hàm rút tiền
def withdraw(card_no, amount):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Trang15042005",   # thay bằng mật khẩu MySQL thật của bạn
        database="atm_demo"
    )
    cur = conn.cursor()
    try:
        conn.start_transaction()

        # Lấy số dư hiện tại
        cur.execute("""
            SELECT account_id, balance 
            FROM accounts 
            JOIN cards USING(account_id) 
            WHERE card_no=%s 
            FOR UPDATE
        """, (card_no,))
        result = cur.fetchone()
        if not result:
            raise Exception("Card not found")
        account_id, balance = result

        # Kiểm tra số dư
        if balance < amount:
            raise Exception("Insufficient funds")

        # Cập nhật số dư
        cur.execute("UPDATE accounts SET balance = balance - %s WHERE account_id = %s",
                    (amount, account_id))

        # Lưu transaction log
        cur.execute("""
            INSERT INTO transactions(account_id, card_no, atm_id, tx_type, amount, balance_after) 
            VALUES(%s, %s, 1, 'WITHDRAW', %s, %s)
        """, (account_id, card_no, amount, balance - amount))

        conn.commit()
        print("Withdraw success")

    except Exception as e:
        conn.rollback()
        print("Error:", e)

    finally:
        conn.close()

# Demo chạy thử
if __name__ == "__main__":
    card_no = "12345678"
    pin = "1234"

    if verify_pin(card_no, pin):
        withdraw(card_no, 200)
    else:
        print("Invalid PIN")
