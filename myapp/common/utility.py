"""
# ユーティリティ
# myapp.common.utility
#
# Pythonのめんどくさいとこ簡単にするのとか
# アプリケーションに依存しないもの
"""
import os
from types import FunctionType


def import_(module_name: str) -> "module":
	"""
	# 動的インポート
	@param module_name: モジュール名(mypackage.subpackage.mymodule)
	"""
	try:
		mod = __import__(module_name)  # PENDING impモジュール？
		components = module_name.split('.')
		for c in components[1:]:
			mod = getattr(mod, c)
		return mod
	except (ImportError, AttributeError):
		return None


def call_recursive_directory(func: FunctionType, dir_: str) -> None:
	"""
	再帰的にディレクトリ内のファイルに処理を行う
	@param func: function(file_path: str) ファイルパス文字列を引数に持つ関数オブジェクト
	@param dir_: ディレクトリパス文字列
	"""
	#translationME クラス説明英語化
	for basename in os.listdir(dir_):
		path = os.path.join(dir_, basename)
		if not basename.startswith('_'):  # PENDING 処理対象外ファイル、ディレクトリ名のチェック関数も受け取るか
			if os.path.isdir(path):
				call_recursive_directory(func, path)
			elif os.path.isfile(path):
				func(path)
