"""
共通ユーティリティ単体テスト
"""
import unittest
from myapp.common import utility
from myapp.common import debug


class TestUtility(unittest.TestCase):
	def test_import(self):
		mod = utility.import_('myapp.common.debug')
		self.assertEqual(mod, debug)


if __name__ == '__main__':
	unittest.main()
