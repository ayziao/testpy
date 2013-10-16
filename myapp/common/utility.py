"""
# myapp.common.utility
#
# ユーティリティ
#
# Pythonのめんどくさいとこ簡単にするのとか
"""


def import_(module_name):
	"""
	# 動的インポート
	"""
	try:

		mod = __import__(module_name)
		components = module_name.split('.')
		for c in components[1:]:
			mod = getattr(mod, c)

		return mod

	except (ImportError, AttributeError):
		return None

