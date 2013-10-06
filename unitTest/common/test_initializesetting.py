import unittest
import os

path = os.path.dirname(os.path.abspath(__file__))

from myapp.common import initializesetting


class TestInitializeSetting(unittest.TestCase):
	def test_ini(self):
		initializesetting.set_config_directory(path + '/../config/')
		conf = initializesetting.get_ini('test')
		self.assertEqual(conf['test'], 'test')


if __name__ == '__main__':
	unittest.main()
