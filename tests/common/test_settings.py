"""
共通設定単体テスト
"""
import unittest
import os
from datetime import datetime

path = os.path.dirname(os.path.abspath(__file__))

from myapp.common import settings

#PENDING メソッド以外のテスト（初期化とか）もテスト必要か考える


class TestSettings(unittest.TestCase):
	def test_get_ini(self):
		#セクション指定
		settings.set_config_path(path + '/../config/')
		conf = settings.get_ini('test')
		self.assertEqual(conf['test'], 'test')

		#セクション指定なし
		conf = settings.get_ini()
		conf2 = conf['test']
		self.assertEqual(conf2['test'], 'test')

		#存在しないセクション
		conf = settings.get_ini('nothing_section')
		self.assertIsNone(conf)

	def test_get_ini_path(self):
		path_ = settings._get_ini_path()
		self.assertTrue(path_.find('setting.ini') > 0)

	def test_default_path(self):
		path = os.path.dirname(os.path.abspath(__file__))
		test = str(path.replace('tests/common', '')) + 'config/setting.ini'
		defpath = settings._default_path()
		self.assertEqual(test, defpath)

	def test_time(self):
		aaa = datetime.utcnow()
		tstr = aaa.strftime('%Y%m%d%H%M%S%f')

	#PENDING どうしましょう
	# print(tstr)


if __name__ == '__main__':
	unittest.main()
