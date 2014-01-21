import unittest

from myapp.common import database
from myapp.model.useraccount import UserAccount


class TestUserAccount(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#database.get_connection('/var/tmp/test.sqlite3db')  # PENDING 引数仮
		database.get_connection(':memory:')  # PENDING 引数仮
		UserAccount.create_table()

		#テストデータインサート
		database.connection.executemany("insert into UserAccount values (?, ?, ?, ?, ?)", [
			("test", 'hoge@piyo.com', 'aaaa', '2012-12-31 23:59:59.123456', '2012-12-31 23:59:59.123456')])

	@classmethod
	def tearDownClass(cls):
		UserAccount.commit()
		database.connection.close()

	def setUp(self):
		self.obj = UserAccount()

	def test_init(self):
		obj = UserAccount()
		self.assertIsInstance(obj, UserAccount)
		self.assertEqual(obj.identifier, '')

		obj = UserAccount('test')
		self.assertEqual(obj.identifier, 'test')
