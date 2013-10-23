import unittest
import os

path = os.path.dirname(os.path.abspath(__file__))

from myapp.common import settings

#PENDING メソッド以外のテスト（初期化とか）もテスト必要か考える


class TestSettings(unittest.TestCase):
	def test_get_ini(self):
		settings.set_config_path(path + '/../config/')
		conf = settings.get_ini('test')
		self.assertEqual(conf['test'], 'test')

	def test_get_ini_path(self):
		path = settings._get_ini_path()
		self.assertTrue(path.find('setting.ini') > 0)


if __name__ == '__main__':
	unittest.main()
