"""
テスト全実行

testsディレクトリ内(サブディレクトリも)のtest_なんとか.pyを実行
"""
import sys
import os
import imp
import unittest


path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path.rstrip('/tests'))

from myapp.common import settings
from myapp.common import utility

settings.set_config_path(path + '/config/')
settings.setting_encode()


def run() -> None:
	"""
	実行
	"""
	suite = unittest.TestSuite()
	loader = unittest.TestLoader()

	#ディレクトリ内のtest_なんとか.pyをテストスイートに追加
	def _add_test(path_):
		file = os.path.basename(path_)
		if file.startswith('test_') and file.endswith('.py'):
			mod = imp.load_source(os.path.splitext(file)[0], path_)
			suite.addTest(loader.loadTestsFromModule(mod))

	utility.call_recursive_directory(_add_test, os.path.curdir) #ディレクトリ内(サブディレクトリ含む)のファイルに実行

	unittest.TextTestRunner(verbosity=2).run(suite) #テスト実行


if __name__ == "__main__":
	run()
