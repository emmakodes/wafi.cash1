import unittest
# from .models import User, users
from models import users
from views import add_user, deposit_money, send_money, check_balance, transfer_money_out

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.first_user = add_user('First User')
        self.second_user = add_user('Second User')

    def test_add_user(self):
        self.assertEqual(len(users), 2)

    def test_deposit_money(self):
        deposit_money(self.first_user, 100)
        self.assertEqual(self.first_user.balance, 100)

    def test_send_money(self):
        deposit_money(self.first_user, 100)
        send_money(self.first_user, self.second_user, 50)
        self.assertEqual(self.first_user.balance, 50)
        self.assertEqual(self.second_user.balance, 50)

    def test_check_balance(self):
        deposit_money(self.first_user, 100)
        self.assertEqual(check_balance(self.first_user), 100)

    def test_transfer_money_out(self):
        deposit_money(self.first_user, 100)
        transfer_money_out(self.first_user, 50)
        self.assertEqual(self.first_user.balance, 50)

if __name__ == '__main__':
    unittest.main()
