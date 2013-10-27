# タスク書き方
# TODO やること
# PENDING 考えること

# タスク
# TODO
# PENDING	全体的な進め方
# PENDING	準備
# PENDING		ストレージ検討 KVS RDB SQLite
# PENDING		プラグインディレクトリ構成
# PENDING		TwitterAPI関連調べる
# PENDING	設計 やることコードに書く
# PENDING	単体テスト 確認することテストコードに書く
# PENDING	実装 単体テスト先に書く
# PENDING	結合テスト
# PENDING デプロイ方法 自動化？
# PENDING
# PENDING myappディレクトリ以下を一切弄らずに設定は変えられるように 設定パスをmain.pyに引数で渡せるようにすべきか？
# PENDING mysql使う前にSQLiteやる？
# PENDING テンプレートエンジン使うか全部DOM操作でやるか
# PENDING loggingモジュール調べる
# PENDING
# PENDING wsgi clientテストするか考える


import unittest
import sys
import os


path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path.rstrip('/tests'))

from myapp.common import settings

settings.set_config_path(path + '/config/')
settings.setting_encode()

from myapp.main import main
from myapp import wsgiclient


top_body = """('Content-Type', 'text/html; charset=utf-8')
200 OK
Hello world!"""

#	'Hello world!'  # PENDING パラメータなんもなしの時の表示考える


class TestMyapp(unittest.TestCase):
	def test_main(self):
		ref = main()
		self.assertEqual(ref, top_body)

	def test_wsgiclient(self):
		def callbuck(a, b):
			self.assertEqual(a, '200 OK')
			test = [('Content-Type', 'text/html; charset=utf-8')]
			self.assertEqual(b, test)

		env = {'PATH_INFO': '/'}
		res = wsgiclient.application(env, callbuck)
		tes_res = ['Hello world!'.encode()]
		self.assertEqual(res, tes_res)


	def test_wsgi_favicon(self):
		def callbuck(a, b):
			self.assertEqual(a, '404 Not Found')
			test = [('Content-Type', 'text/html; charset=utf-8')]
			self.assertEqual(b, test)

		env = {'PATH_INFO': '/favicon.ico'}
		res = wsgiclient.application(env, callbuck)
		tes_res = ['Not Found'.encode()]
		self.assertEqual(res, tes_res)


if __name__ == '__main__':
	unittest.main()
