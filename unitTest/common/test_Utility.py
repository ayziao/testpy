import unittest
from myapp.common import Utility

#PENDING テスト書くかちゃんと置くとこ考える
#TODO エラーなおす パス関連？

class MyTestCase(unittest.TestCase):
	def test_load_conf(self):
		#TODO 設定ファイルをサンプルじゃないの読み込み
		#PENDING テスト時とデバッグ時と通常時で読み込む設定ファイルを変える
		conf = Utility.load_conf()
		str = conf['section']['key']
		print(conf)
		self.assertEqual(str, 'value')


if __name__ == '__main__':
	unittest.main()
