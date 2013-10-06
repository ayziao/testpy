import unittest
import os

path = os.path.dirname(os.path.abspath(__file__))

import myapp.common.initializesetting as ini


class initializesetting(unittest.TestCase):
	def test_ini(self):
		ini.set_config_directory(path + '/../config/')
		conf = ini.get_ini('test')
		self.assertEqual(conf['test'], 'test')


if __name__ == '__main__':
	unittest.main()
