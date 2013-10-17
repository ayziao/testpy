"""
# myapp.common.request
"""

_instance = []


class Request():
	"""
	# リクエスト
	#
	# HTTPリクエストに限らずコマンドラインからの実行でも使う
	"""

	def __init__(self):
		self.path = ''
		self.extension = 'html'  # 出力形式(拡張子)
		self.command = ''  # ユーザーコマンド
		self.parameter = ''  # ユーザーパラメータ
		self.input = ''  # ユーザ入力(ファイルとか プロパティはガワだけで処理を入れる コールバック関数？)
		self.system_command = ''  # システムコマンド
		self.system_parameter = ''  # システムパラメータ
		self.system_input = ''  # システム入力(コールバック関数？)
		self.paging = None
		self.controller_class_name = ''
		self.method_name = ''


def get_instance() -> Request:
	"""
	# 最新のスタックを返す 空なら作ってセット
	"""
	if not _instance:
		_instance.append(Request())

	return _instance[-1]


def create_instance() -> Request:
	"""
	# 新しくスタック積んで返す
	"""
	_instance.append(Request())

	return _instance[-1]


def pop_instance() -> Request:
	"""
	# 最新のスタックを取り出して返す
	"""
	if _instance:
		return _instance.pop()
	else:
		return None

