import unittest
from unittest.mock import patch, MagicMock
import hashlib
from lab07_withdraw_module import atm


class TestVerifyPin(unittest.TestCase):
    @patch("lab07_withdraw_module.atm.mysql.connector.connect")
    def test_verify_pin_correct(self, mock_connect):
        conn = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = conn
        conn.cursor.return_value = cur

        card_no = "CARD123"
        pin = "1234"
        cur.fetchone.return_value = (hashlib.sha256(pin.encode()).hexdigest(),)

        result = atm.verify_pin(card_no, pin)

        self.assertTrue(result)

    @patch("lab07_withdraw_module.atm.mysql.connector.connect")
    def test_verify_pin_wrong(self, mock_connect):
        conn = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = conn
        conn.cursor.return_value = cur

        card_no = "CARD123"
        pin = "1234"
        cur.fetchone.return_value = (hashlib.sha256(b"9999").hexdigest(),)

        result = atm.verify_pin(card_no, pin)

        self.assertFalse(result)


class TestWithdraw(unittest.TestCase):
    @patch("builtins.print")
    @patch("lab07_withdraw_module.atm.mysql.connector.connect")
    def test_withdraw_success(self, mock_connect, mock_print):
        conn = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = conn
        conn.cursor.return_value = cur

        card_no = "CARD1001"
        amount = 200
        cur.fetchone.return_value = (1, 1000)  # đủ tiền

        atm.withdraw(card_no, amount)

        conn.commit.assert_called_once()
        conn.rollback.assert_not_called()
        mock_print.assert_any_call("Withdraw success")

    @patch("builtins.print")
    @patch("lab07_withdraw_module.atm.mysql.connector.connect")
    def test_withdraw_insufficient(self, mock_connect, mock_print):
        conn = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = conn
        conn.cursor.return_value = cur

        card_no = "CARD123"
        amount = 500
        cur.fetchone.return_value = (1, 100)  # không đủ tiền

        atm.withdraw(card_no, amount)

        conn.rollback.assert_called_once()
        conn.commit.assert_not_called()
        mock_print.assert_any_call("Error:", unittest.mock.ANY)


if __name__ == "__main__":
    unittest.main()