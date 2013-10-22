# タスク書き方
# TODO やること
# PENDING 考えること

# タスク
# TODO coverage.py調べる
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
# PENDING ユニットテストもコンソールから実行できるようにパス解決するか
# PENDING myappディレクトリ以下を一切弄らずに設定は変えられるように 設定パスをmain.pyに引数で渡せるようにすべきか？
# PENDING mysql使う前にSQLiteやる？
# PENDING テンプレートエンジン使うか全部DOM操作でやるか
# PENDING loggingモジュール調べる
# PENDING
# PENDING wsgi clientテストするか考える


import unittest
import sys
import os
from pprint import pprint


path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path.rstrip('/unitTest'))
sys.path.append(path.rstrip('/unitTest') + '/myapp')
pprint(sys.path)

from myapp.common import settings

settings.set_config_path(path + '/config/')
settings.setting_encode()

from myapp.main import main

top_body = 'Hello world!'  # PENDING パラメータなんもなしの時の表示考える


class TestMyapp(unittest.TestCase):
	def test_main(self):
		ref = main()
		self.assertEqual(ref.status, '200 OK')
		self.assertEqual(ref.body, top_body)


if __name__ == '__main__':
	unittest.main()
