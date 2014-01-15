"""
共通設定単体テスト
"""
import unittest
import os

path = os.path.dirname(os.path.abspath(__file__))

from myapp.common import settings

#PENDING メソッド以外のテスト（初期化とか）もテスト必要か考える


class TestSettings(unittest.TestCase):
	def test_get_ini(self):
		#セクション指定なし
		conf = settings.get_ini()
		conf2 = conf['test']
		self.assertEqual(conf2['test'], 'test')

	def test_get_ini_section(self):
		#セクション指定
		settings.set_config_path(path + '/../config/')
		conf = settings.get_ini('test')
		self.assertEqual(conf['test'], 'test')

	def test_get_ini_section_nothing_section(self):
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

	def test_read_ini(self):
		settings._read_ini(settings._get_ini_path() + '.sample')
		ini = settings.get_ini('application')
		self.assertEqual('false', ini.get('debug'))

	def test_get_ini_path_none(self):
		bk = settings._config_path

		settings._config_path = None
		path = settings._get_ini_path()

		settings._config_path = bk

		self.assertTrue(path.endswith('testpy/config/setting.ini'))


if __name__ == '__main__':
	unittest.main()
