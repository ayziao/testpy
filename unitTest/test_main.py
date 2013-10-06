# タスク書き方
# TODO やること
# PENDING 考えること

# タスク
# PENDING	全体的な進め方
# PENDING	準備
# PENDING		webサーバどうにかする
# PENDING		ストレージ検討 KVS RDB
# PENDING		プラグインディレクトリ構成
# PENDING		TwitterAPI関連調べる
# PENDING	設計
# PENDING	単体テスト
# PENDING	実装
# PENDING	結合テスト
# PENDING
# PENDING ユニットテストもコンソールから実行できるようにパス解決するか
# PENDING myappディレクトリ以下を一切弄らずに設定は変えられるように 設定パスをmain.pyに引数で渡せるようにすべきか？
# PENDING mysql使う前にsqliteやる？
# PENDING テンプレートエンジン使うか全部DOM操作でやるか
# PENDING
# PENDING
# PENDING wsgiclientテストするか考える
#from myapp.wsgiclient import application
#def test_application(self):
#	def st(aaa, bbb):
#		pass
#
#	env = {'PATH_INFO': '/favicon.ico', 'debug': False}  # TODO デバッグ表示オフ機能つける
#	ret = application(env, st)
#	self.assertEqual(ret, [top_body.encode("utf-8")])


import unittest
import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)

import myapp.common.initializesetting as ini

ini.set_config_directory(path + '/config/')
ini.get_ini()

from myapp.myapp_main import main

top_body = 'Hello world!'  # PENDING パラメータなんもなしの時の表示考える


class myapp(unittest.TestCase):
	def test_main(self):
		ref = main()
		self.assertEqual(ref.status, '200 OK')
		self.assertEqual(ref.body, top_body)


if __name__ == '__main__':
	unittest.main()
