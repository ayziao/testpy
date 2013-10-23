import os
import sys


path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path.rstrip('/unitTest'))

from myapp.common import settings

settings.set_config_path(path + '/config/')
settings.setting_encode()

from setuptools.command.test import test as TestCommand
from setuptools import setup


class PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True

	def run_tests(self):
		import pytest

		errno = pytest.main(self.test_args)
		sys.exit(errno)


setup(
	tests_require=['mock', 'pytest'],
	cmdclass={'test': PyTest},
)





#def load_testpy(path, suite, loader):
#	for file in os.listdir(path):
#		path_file = path + '/' + file
#		if os.path.isdir(path_file) and not file.startswith('_'):
#			load_testpy(path_file, suite, loader)
#		elif os.path.isfile(path_file) and file.startswith('test_') and file.endswith('.py'):
#			mod = imp.load_source(os.path.splitext(file)[0], path_file)
#			suite.addTest(loader.loadTestsFromModule(mod))
#	pass
#
#
#if __name__ == "__main__":
#	suite = unittest.TestSuite()
#	loader = unittest.TestLoader()
#	load_testpy(os.path.curdir, suite, loader)
#	unittest.TextTestRunner(verbosity=2).run(suite)