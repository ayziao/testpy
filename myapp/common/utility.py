"""
# ユーティリティ
#
"""


def import_(module_name):
	mod = __import__(module_name)
	components = module_name.split('.')
	for c in components[1:]:
		mod = getattr(mod, c)
	return mod