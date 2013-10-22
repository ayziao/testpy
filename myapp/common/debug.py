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
from myapp.common.response import Response


_messages = OrderedDict()
_mode = False


def mode(mode_):
	global _mode
	_mode = mode_


class Debug:
	"""
	# デバッグ用
	"""
	# TODO クラスやめてモジュールにする

	def __init__(self) -> None:
		global _messages
		_messages = OrderedDict()
		self.append_message('debug', settings.get_ini('application')['debug'])

	def get_messages(self):
		return _messages

	def append_message(self, name: str, obj) -> None:
		"""
		# デバッグメッセージを追加
		@param name: 辞書に入れる名前
		@param obj: なんでも
		@return:
		"""
		_messages[name] = obj

	def print_2(self) -> None:
		if not settings.environ is None \
			and settings.environ['PATH_INFO'] == '/favicon.ico':
			pass
		else:
			self._collect()
			p.pprint(_messages)
			self.__init__()


	def print(self, res: Response):
		if _mode == 'head':
			_debug_print_head(self, res)
		elif _mode == 'body':
			_debug_print_body(self, res)
		else:
			self.print_2()

		pass

	def messages_to_str(self) -> None:
		if not settings.environ is None \
			and settings.environ['PATH_INFO'] == '/favicon.ico':
			pass
		else:
			self._collect()
			pf = p.pformat(_messages)
			self.__init__()
			return pf


	def message_to_http_head(self, prefix: str) -> None:
		if not settings.environ is None \
			and settings.environ['PATH_INFO'] == '/favicon.ico':
			return None
		else:
			self._collect()
			out_list = self._dict_format(_messages, prefix)
			self.__init__()
			return out_list


	def _dict_format(self, dict_: OrderedDict, prefix: str) -> OrderedDict:
		ddd = OrderedDict()
		index = 0
		for key_, item_ in dict_.items():
			index += 1
			key_str = prefix + '-' + key_
			if isinstance(item_, dict) or isinstance(item_, OrderedDict):
				ddd.update(self._dict_format(item_, key_str))
			else:
				ddd[key_str] = p.pformat(item_)
		return ddd


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


def _debug_print_head(debug_: Debug, res: Response) -> None:
	list_ = debug_.message_to_http_head('X-DEBUG')
	if list_:
		for key_, item_ in list_.items():
			res.headers.append((key_, item_))


def _debug_print_body(debug_: Debug, res: Response) -> None:
	str_ = debug_.messages_to_str()
	res.body += "\n<hr><pre>\n" + str(str_) + "</pre>"


if __name__ == '__main__':
	res = Response()
	Debug().print(res)
