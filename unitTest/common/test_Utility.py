import unittest
from myapp.common import Utility


class MyTestCase(unittest.TestCase):
	def test_load_conf(self):
		#TODO 設定ファイルの読み込みを相対パスじゃなくする
		#TODO 設定ファイルをサンプルじゃないの読み込み
		#PENDING テスト時とデバッグ時と通常時で読み込む設定ファイルを変える
		conf = Utility.load_conf()
		str = conf['section']['key']
		print(conf)
		self.assertEqual(str, 'value')


if __name__ == '__main__':
	unittest.main()
