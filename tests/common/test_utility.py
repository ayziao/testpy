"""
共通ユーティリティ単体テスト
"""
import os
import unittest
from myapp.common import utility
from myapp.common import debug


class TestUtility(unittest.TestCase):
	def test_import(self):
		mod = utility.import_('myapp.common.debug')
		self.assertEqual(mod, debug)

	def test_call_recursive_directory(self):
		list_ = []

		def _add_test(path_):
			file = os.path.basename(path_)
			if file.startswith('test_') and file.endswith('.py'):
				list_.append(file)

		path = os.path.dirname(os.path.abspath(__file__))

		utility.call_recursive_directory(_add_test, path.rstrip('/common')) #ディレクトリ内(サブディレクトリ含む)のファイルに実行

		self.assertEqual(list_.__str__(),
		                 "['test_application.py', 'test_database.py', 'test_debug.py', 'test_request.py', 'test_response.py', 'test_settings.py', 'test_utility.py', 'test_account.py', 'test_content.py', 'test_data.py', 'test_top.py', 'test_basedata.py', 'test_main.py', 'test_timeline.py', 'test_top.py']")


if __name__ == '__main__':
	unittest.main()
