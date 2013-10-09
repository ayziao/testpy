class Request():
	def __init__(self):
		self.path = ''
		self.extension = 'html' # 出力形式(拡張子)
		self.command = '' # ユーザーコマンド
		self.parameter = '' # ユーザーパラメータ
		self.input = '' # ユーザ入力(ファイルとか プロパティはガワだけで処理を入れる コールバック関数？)
		self.systemCommand = '' # システムコマンド
		self.systemParameter = '' # システムパラメータ
		self.systemInput = '' # システム入力(コールバック関数？)
		self.paging = ''
		self.controllerClassName = ''
		self.methodName = ''
