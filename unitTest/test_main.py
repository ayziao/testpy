# タスク書き方
# TODO やること
# PENDING 考えること

# タスク
# TODO coverage.py調べる
# TODO
# TODO
# TODO
# PENDING	全体的な進め方
# PENDING	準備
# PENDING		ストレージ検討 KVS RDB SQLite
# PENDING		プラグインディレクトリ構成
# PENDING		TwitterAPI関連調べる
# PENDING	設計
# PENDING	単体テスト
# PENDING	実装
# PENDING	結合テスト
# PENDING
# PENDING ユニットテストもコンソールから実行できるようにパス解決するか
# PENDING myappディレクトリ以下を一切弄らずに設定は変えられるように 設定パスをmain.pyに引数で渡せるようにすべきか？
# PENDING mysql使う前にSQLiteやる？
# PENDING テンプレートエンジン使うか全部DOM操作でやるか
# PENDING
# PENDING
# PENDING wsgi clientテストするか考える


import unittest
import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)

from myapp.common import settings

settings.config_path = path + '/config/'

from myapp.myapp_main import main

top_body = 'Hello world!'  # PENDING パラメータなんもなしの時の表示考える


class TestMyapp(unittest.TestCase):
	def test_main(self):
		ref = main()
		self.assertEqual(ref.status, '200 OK')
		self.assertEqual(ref.body, top_body)


if __name__ == '__main__':
	unittest.main()
