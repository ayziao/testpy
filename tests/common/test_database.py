"""
データベース単体テスト
"""

import unittest
from myapp.common import database


class MyTestCase(unittest.TestCase):
	def test_something(self):
		self.assertIsNone(database.connection)

# PENDING データベースアプリを何にするか sqlite Postgres キーバリューストア
# PENDING トランザクションの仕組みはどうするか
# PENDING 複数サーバ 複数DB を考慮するか

if __name__ == '__main__':
	unittest.main()
