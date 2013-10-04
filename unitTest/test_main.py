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
# PENDING
# PENDING
# PENDING


import unittest

from myapp.myapp_main import application
from myapp.myapp_main import main


top_body = 'value Hello world!'  # PENDING パラメータなんもなしの時の表示考える


class MyTestCase(unittest.TestCase):
	def test_main(self):
		ref = main()
		self.assertEqual(ref.body, top_body)

	def test_application(self):
		def st(aaa, bbb):
			pass

		env = {'PATH_INFO': '/favicon.ico'}  # TODO デバッグ表示オフ機能つける
		ret = application(env, st)
		self.assertEqual(ret, [top_body.encode("utf-8")])


if __name__ == '__main__':
	unittest.main()
