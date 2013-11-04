"""
# 共通 リクエストモジュール
# myapp.common.request
"""


class Request():
	"""
	# リクエスト
	#
	# HTTPリクエストに限らずコマンドラインからの実行でも使う
	"""

	def __init__(self) -> None:
		self.path = ''
		self.extension = 'html'  # 出力形式(拡張子)
		self.command = ''  # ユーザーコマンド
		self.parameter = ''  # ユーザーパラメータ
		self.input = ''  # ユーザ入力(ファイルとか プロパティはガワだけで処理を入れる コールバック関数？)
		self.system_command = ''  # システムコマンド
		self.system_parameter = ''  # システムパラメータ
		self.system_input = ''  # システム入力(コールバック関数？)
		self.paging = None  # ページングクラス入れ
		self.controller_class_name = ''  # コントローラクラス名
		self.method_name = ''  # メソッド名
