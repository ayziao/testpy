import unittest
import os

path = os.path.dirname(os.path.abspath(__file__))

from myapp.common import settings


class TestSettings(unittest.TestCase):
	def test_ini(self):
		settings.config_path = path + '/../config/'
		conf = settings.get_ini('test')
		self.assertEqual(conf['test'], 'test')


if __name__ == '__main__':
	unittest.main()
