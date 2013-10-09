import unittest
import os

path = os.path.dirname(os.path.abspath(__file__))

from myapp.common import settings

#PENDING メソッド以外のテスト（初期化とか）もテスト必要か考える

class TestSettings(unittest.TestCase):
	def test_get_ini(self):
		settings.config_path = path + '/../config/'
		conf = settings.get_ini('test')
		self.assertEqual(conf['test'], 'test')


if __name__ == '__main__':
	unittest.main()
