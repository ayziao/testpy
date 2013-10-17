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


def view_dispatcher(class_name):
	"""
	# ビュー振り分け
	"""
	module_name = 'myapp.view.' + class_name.lower()  # PENDING 名前空間を動的に取る？
	mod = import_(module_name)

	try:
		class_object = getattr(mod, class_name)
		return class_object()
	except AttributeError:
		# PENDING 404?
		return None