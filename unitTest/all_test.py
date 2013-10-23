import imp
import os
import unittest


def load_testpy(path, suite, loader):
	for file in os.listdir(path):
		path_file = path + '/' + file
		if os.path.isdir(path_file) and not file.startswith('_'):
			load_testpy(path_file, suite, loader)
		elif os.path.isfile(path_file) and file.startswith('test_') and file.endswith('.py'):
			mod = imp.load_source(os.path.splitext(file)[0], path_file)
			suite.addTest(loader.loadTestsFromModule(mod))
	pass


if __name__ == "__main__":
	suite = unittest.TestSuite()
	loader = unittest.TestLoader()
	load_testpy(os.path.curdir, suite, loader)
	unittest.TextTestRunner(verbosity=2).run(suite)