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

		path = os.path.dirname(os.path.abspath(__file__)).rstrip('/common')

		utility.call_recursive_directory(_add_test, path)  # ディレクトリ内(サブディレクトリ含む)のファイルに実行

		list_.sort()

		assertlist = []
		assertlist.append('test_application.py')
		assertlist.append('test_database.py')
		assertlist.append('test_debug.py')
		assertlist.append('test_request.py')
		assertlist.append('test_response.py')
		assertlist.append('test_settings.py')
		assertlist.append('test_utility.py')
		assertlist.append('test_account.py')
		assertlist.append('test_content.py')
		assertlist.append('test_data.py')
		assertlist.append('test_top.py')
		assertlist.append('test_basedata.py')
		assertlist.append('test_main.py')
		assertlist.append('test_timeline.py')
		assertlist.append('test_top.py')
		assertlist.append('test_useraccount.py')
		assertlist.sort()

		self.assertEqual(list_.__str__(), assertlist.__str__())


if __name__ == '__main__':
	unittest.main()
