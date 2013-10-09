"""
# myapp.common.debug
"""
import sys
import resource
from pprint import pprint
from datetime import datetime

from myapp.common import settings


class Debug:
	"""
	# デバッグ用 単体テストは書かない
	"""

	@staticmethod
	def print():
		pprint({'arg': sys.argv})
		if settings.environ is not None and settings.environ[
			'PATH_INFO'] != '/favicon.ico':
			pprint(settings.environ)
		ru = resource.getrusage(resource.RUSAGE_SELF)
		print('メモリ : ' + str(ru.ru_maxrss))
		now = datetime.utcnow()
		dif = now - settings.start_time
		print(settings.start_time)
		print(now)
		print(dif)


if __name__ == '__main__':
	Debug.print()
