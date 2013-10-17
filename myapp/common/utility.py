"""
# myapp.common.utility
#
# ユーティリティ
#
# Pythonのめんどくさいとこ簡単にするのとか
# アプリケーションに依存しないもの
"""


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

