"""
# myapp.common.debug
"""
import resource
from pprint import pprint
from datetime import datetime

from myapp.common import settings


class Debug:
	"""
	# デバッグ用
	"""

	def __init__(self):
		self.list = []
		self.append_message('debug', settings.get_ini('application')['debug'])


	def append_message(self, name, obj):
		if name == '':
			self.list.append(obj)
		else:
			self.list.append({name: obj})


	def collect(self):
		now = datetime.utcnow()
		self.append_message('arg', settings.arg)
		if settings.environ is not None:
			if settings.environ['PATH_INFO'] != '/favicon.ico':
				self.append_message('env', settings.environ)
		ru = resource.getrusage(resource.RUSAGE_SELF)
		self.append_message('memory', ru.ru_maxrss)
		self.append_message('start_time', settings.start_time)
		self.append_message('end_time', now)
		self.append_message('dif', now - settings.start_time)


	def print(self):
		if settings.environ is None:
			self.collect()
			pprint(self.list)
		elif settings.environ['PATH_INFO'] != '/favicon.ico':
			self.collect()
			pprint(self.list)


if __name__ == '__main__':
	Debug().print()
