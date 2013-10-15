"""
# ユーティリティ
#
# Pythonのめんどくさいとこ簡単にするのとか
"""


def import_(module_name):
	try:
		mod = __import__(module_name)
	except ImportError:
		return None

	components = module_name.split('.')
	for c in components[1:]:
		try:
			mod = getattr(mod, c)
		except AttributeError:
			return None

	return mod