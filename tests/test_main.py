"""
メインテスト
"""
# タスク書き方
# TODO やること
# PENDING 考えること

# タスク
# TODO
# PENDING	全体的な進め方 要件書く データ設計する クラス設計する コメント書く テスト書く 実装書く
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
# PENDING Postgres調査
# PENDING テンプレートエンジン使うか全部DOM操作でやるか
# PENDING loggingモジュール調べる
# PENDING


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
Hello world! top"""

#	'Hello world!'  # PENDING パラメータなんもなしの時の表示考える


class TestMyapp(unittest.TestCase):
	# PENDING 引数や設定みてヘッダ出さないとか入れる
	#python myapp/main.py
	#データパス
	#リクエスト	(ｗｅｂと同じ)
	#コマンド（コマンドライン独自 webでHTTTPヘッダに出してる情報どうするかとか）

	def test_main(self):
		ref = main()
		self.assertEqual(ref, top_body)

	def test_wsgiclient(self):
		settings.environ = None

		def _callback(a, b):
			self.assertEqual(a, '200 OK')
			test = [('Content-Type', 'text/html; charset=utf-8')]
			self.assertEqual(b, test)

		tes_res = '<html>'
		#tes_res = 'hello '

		env = {'PATH_INFO': '/'}
		res = wsgiclient.application(env, _callback)
		res2 = res[0].decode()
		self.assertEqual(res2[0:6], tes_res)
		settings.environ = None


	def test_wsgi_favicon(self):
		settings.environ = None

		def _callback(a, b):
			self.assertEqual(a, '404 Not Found')
			test = [('Content-Type', 'text/html; charset=utf-8')]
			self.assertEqual(b, test)

		env = {'PATH_INFO': '/favicon.ico'}
		res = wsgiclient.application(env, _callback)
		tes_res = ['Not Found'.encode()]
		self.assertEqual(res, tes_res)
		settings.environ = None


if __name__ == '__main__':
	unittest.main()
