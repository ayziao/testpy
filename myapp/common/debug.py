"""
# myapp.common.debug
"""
from pprint import pprint


class Debug:
	"""
	# デバッグ用 単体テストは書かない
	"""

	def print(self):
	#		g = globals()
	#		del g['__builtins__']
		pprint(globals())
		pass


if __name__ == '__main__':
	c = Debug()
	c.print()
