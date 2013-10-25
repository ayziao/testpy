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
	append_message('debug', _mode)


def clear_message() -> None:
	global _messages
	_messages = OrderedDict()
	append_message('debug', _mode)


def get_message_dic() -> OrderedDict:
	return _messages


def append_message(name: str, obj) -> None:
	"""
	# デバッグメッセージを追加
	@param name: 辞書に入れる名前
	@param obj: なんでも
	@return:
	"""
	_messages[name] = obj


def _message_to_stdout() -> None:
	if not settings.environ is None \
		and settings.environ['PATH_INFO'] == '/favicon.ico':
		pass
	else:
		_collect()
		p.pprint(_messages)
		clear_message()


def output_message(res_: Response):
	if _mode == 'head':
		_debug_print_head(res_)
	elif _mode == 'body':
		_debug_print_body(res_)
	else:
		_message_to_stdout()

	pass


def _messages_to_str() -> None:
	if not settings.environ is None \
		and settings.environ['PATH_INFO'] == '/favicon.ico':
		pass
	else:
		_collect()
		pf = p.pformat(_messages)
		clear_message()
		return pf


def _message_to_http_head(prefix: str) -> None:
	if not settings.environ is None \
		and settings.environ['PATH_INFO'] == '/favicon.ico':
		return None
	else:
		_collect()
		out_list = _dict_format(_messages, prefix)
		clear_message()
		return out_list


def _dict_format(dict_: OrderedDict, prefix: str) -> OrderedDict:
	ddd = OrderedDict()
	index = 0
	for key_, item_ in dict_.items():
		index += 1
		key_str = prefix + '-' + key_
		if isinstance(item_, dict) or isinstance(item_, OrderedDict):
			ddd.update(_dict_format(item_, key_str))
		else:
			ddd[key_str] = p.pformat(item_)
	return ddd


def _collect() -> None:
	now = datetime.utcnow()
	append_message('arg', settings.arg)
	if settings.environ is not None:
		if settings.environ['PATH_INFO'] != '/favicon.ico':
			append_message('env', settings.environ)
	ru = resource.getrusage(resource.RUSAGE_SELF)
	append_message('memory', ru.ru_maxrss)
	append_message('start_time', settings.start_time)
	append_message('end_time', now)
	append_message('dif', now - settings.start_time)


def _debug_print_head(res_: Response) -> None:
	list_ = _message_to_http_head('X-DEBUG')
	if list_:
		for key_, item_ in list_.items():
			res_.headers.append((key_, item_))


def _debug_print_body(res_: Response) -> None:
	str_ = _messages_to_str()
	res_.body += "\n<hr><pre>\n" + str(str_) + "</pre>"


if __name__ == '__main__':
	res = Response()

	#clear_message()
	#mode('body')
	#output_message(res)
	#p.pprint(res.body)
	#
	#clear_message()
	#mode('head')
	#output_message(res)
	#p.pprint(res.headers)

	clear_message()
	mode('true')
	output_message(res)



	# TODO ;debug = context  #CLIならbody webならHeader
	# TODO コード整理する