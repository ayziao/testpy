import unittest


class TestAccount(unittest.TestCase):
	"""
	アカウントコントローラ単体テスト
	"""

	def _get_target_class(self):
		from myapp.controller.account import Account

		return Account

	def _get_target_class_instance(self):
		class_ = self._get_target_class()
		return class_()

	def test_init(self):
		account = self._get_target_class_instance()
		self.assertIsInstance(account, self._get_target_class())

	# PENDING アサート

	def test_signup(self):
		account = self._get_target_class_instance()
		account.signup()
		self.assertTrue(True)

	# PENDING アサート

	def test_login(self):
		account = self._get_target_class_instance()
		account.login()
		self.assertTrue(True)

	# PENDING アサート

	def test_loguout(self):
		account = self._get_target_class_instance()
		account.logout()
		self.assertTrue(True)

	# PENDING アサート
