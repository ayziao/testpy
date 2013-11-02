"""
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


def run():
	"""
	実行
	@return:
	"""
	suite = unittest.TestSuite()
	loader = unittest.TestLoader()

	def _add_test(path_):
		file = os.path.basename(path_)
		if file.startswith('test_') and file.endswith('.py'):
			mod = imp.load_source(os.path.splitext(file)[0], path_)
			suite.addTest(loader.loadTestsFromModule(mod))

	utility.call_recursive_directory(_add_test, os.path.curdir)

	unittest.TextTestRunner(verbosity=1).run(suite)


if __name__ == "__main__":
	run()
