#タスク書き方
#TODO やること
#PENDING 考えること

#タスク
#PENDING	全体的な進め方
#PENDING	準備
#PENDING		webサーバどうにかする
#PENDING		ストレージ検討 KVS RDB
#PENDING		プラグインディレクトリ構成
#PENDING		TwitterAPI関連調べる
#PENDING	設計
#PENDING	単体テスト
#PENDING	実装
#PENDING	結合テスト
#PENDING
#PENDING
#PENDING
#PENDING


import unittest

from myapp.myapp_main import application


class MyTestCase(unittest.TestCase):
	def test_something(self):
		def st(aaa, bbb):
			pass

		self.assertEqual(True, True)
		self.assertEqual(False, False)

		env = {'PATH_INFO': '/favicon.ico'}
		ref = application(env, st)

		self.assertEqual(ref, ['value Hello world!'.encode("utf-8")])


if __name__ == '__main__':
	unittest.main()
