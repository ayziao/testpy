"""
アカウントモデル単体テスト
"""
import unittest

from myapp.controller.account import Account


class TestAccount(unittest.TestCase):
	def test_init(self):
		account = Account()
		self.assertIsInstance(account, Account)

	def test_signup(self):
		account = Account()
		account.signup()
		self.assertTrue(True)

	# PENDING アサート

	def test_login(self):
		account = Account()
		account.login()
		self.assertTrue(True)

	# PENDING アサート
