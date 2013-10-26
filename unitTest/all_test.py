import sys
import os
import imp
import unittest


path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path.rstrip('/unitTest'))

from myapp.common import settings

settings.set_config_path(path + '/config/')
settings.setting_encode()


def load_testpy(path, suite, loader):
	for file in os.listdir(path):
		path_file = path + '/' + file
		if os.path.isdir(path_file) and not file.startswith('_'):
			load_testpy(path_file, suite, loader)
		elif os.path.isfile(path_file) and file.startswith('test_') and file.endswith('.py'):
			mod = imp.load_source(os.path.splitext(file)[0], path_file)
			suite.addTest(loader.loadTestsFromModule(mod))
	pass


def run():
	suite = unittest.TestSuite()
	loader = unittest.TestLoader()
	load_testpy(os.path.curdir, suite, loader)
	unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
	run()