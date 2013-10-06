class Request():
	path = ''
	extension = 'html' # 出力形式(拡張子)
	command = '' # ユーザーコマンド
	parameter = '' # ユーザーパラメータ
	input = '' # ユーザ入力(ファイルとか プロパティはガワだけで処理を入れる コールバック関数？)
	systemCommand = '' # システムコマンド
	systemParameter = '' # システムパラメータ
	systemInput = '' # システム入力(コールバック関数？)
	paging = ''
	controllerClassName = ''
	methodName = ''
