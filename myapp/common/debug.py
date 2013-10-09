"""
# myapp.common.debug
"""
import sys
import resource
from io import StringIO
from pprint import pprint
from datetime import datetime

from myapp.common import settings


class Debug:
	"""
	# デバッグ用
	"""

	@staticmethod
	def print():
		stdout = StringIO()
		pprint({'arg': sys.argv}, stream=stdout)
		if settings.environ is not None:
			if settings.environ['PATH_INFO'] != '/favicon.ico':
				pprint(settings.environ, stream=stdout)
		ru = resource.getrusage(resource.RUSAGE_SELF)
		print('memory : ' + str(ru.ru_maxrss), file=stdout)
		now = datetime.utcnow()
		dif = now - settings.start_time

		print(settings.start_time, file=stdout)
		print(now, file=stdout)
		print(dif, file=stdout)
		val = stdout.getvalue().encode("utf-8")

	#		print(val)


if __name__ == '__main__':
	Debug.print()
