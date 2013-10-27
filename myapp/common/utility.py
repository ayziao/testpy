"""
# ユーティリティ
# myapp.common.utility
#
# Pythonのめんどくさいとこ簡単にするのとか
# アプリケーションに依存しないもの
"""
import os


def import_(module_name: str) -> "module":
	"""
	# 動的インポート
	@param module_name: モジュール名(myapplication.subdirectory.mymodule)
	"""
	try:

		mod = __import__(module_name)
		components = module_name.split('.')
		for c in components[1:]:
			mod = getattr(mod, c)

		return mod

	except (ImportError, AttributeError):
		return None


def recursive_directory(dir_: str, func: 'function(file_path: str)') -> None:
	"""
	#translationME 再帰的にディレクトリ内のファイルに処理を行う
	@param dir_: ディレクトリパス文字列
	@param func: ファイルパス文字列を引数に持つ関数オブジェクト
	"""
	for basename in os.listdir(dir_):
		path = dir_ + '/' + basename
		if not basename.startswith('_'):  # FIXME 処理対象外ファイル、ディレクトリ名のチェック関数も受け取るか
			if os.path.isdir(path):
				recursive_directory(path, func)
			elif os.path.isfile(path):
				func(path)
