"""
# デバッグ
#
# myapp.common.debug
"""
import resource
import pprint as p
from datetime import datetime
from collections import OrderedDict

from myapp.common import settings


class Debug:
	"""
	# デバッグ用
	"""
	# PENDING クラスにする必要ある？

	def __init__(self) -> None:
		self.list = OrderedDict()
		self.append_message('debug', settings.get_ini('application')['debug'])

	def append_message(self, name: str, obj) -> None:
		"""
		# デバッグメッセージを追加
		@param name: 辞書に入れる名前
		@param obj: なんでも
		@return:
		"""
		self.list[name] = obj

	def print(self) -> None:
		if not settings.environ is None \
			and settings.environ['PATH_INFO'] == '/favicon.ico':
			pass
		else:
			self._collect()
			p.pprint(self.list)
			self.__init__()

	def list_to_str(self) -> None:
		if not settings.environ is None \
			and settings.environ['PATH_INFO'] == '/favicon.ico':
			pass
		else:
			self._collect()
			pf = p.pformat(self.list)
			self.__init__()
			return pf


	def _dict_format(self, dict_: OrderedDict) -> OrderedDict:
		ddd = OrderedDict()
		for key_, item_ in dict_.items():
			if isinstance(item_, dict) or isinstance(item_, OrderedDict):
				ddd.update(self._dict_format(item_))
			else:
				ddd[key_] = p.pformat(item_)
		return ddd


	def get_list(self) -> None:
		if not settings.environ is None \
			and settings.environ['PATH_INFO'] == '/favicon.ico':
			return None
		else:
			self._collect()
			out_list = self._dict_format(self.list)
			self.__init__()
			return out_list


	def _collect(self) -> None:
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


if __name__ == '__main__':
	Debug().print()
