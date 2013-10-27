"""
# デバッグモジュール
# myapp.common.debug
"""
import resource
import pprint as p
from datetime import datetime
from collections import OrderedDict

from myapp.common import settings
from myapp.common.response import Response

_print_mode = False
_messages = OrderedDict()


def set_print_mode(val: str):
	"""
	出力モード設定
	モードはサンプルファイル参照
	@param val: 出力形式
	"""
	global _print_mode
	_print_mode = val
	append_message('debug', val)


def get_message_dic() -> OrderedDict:
	"""
	デバッグメッセージ取得
	@return: 順序有り辞書
	"""
	return _messages


def append_message(name: str, obj) -> None:
	"""
	# デバッグメッセージを追加
	@param name: 辞書に入れる名前
	@param obj: なんでも
	@return: 無し
	"""
	_messages[name] = obj


def output_message(res_: Response):
	"""
	デバッグメッセージ出力
	@param res_: レスポンスインスタンス
	@return:
	"""
	if _print_mode == 'head':
		_debug_print_head(res_)
	elif _print_mode == 'body':
		_debug_print_body(res_)
	else:
		_message_to_stdout()


# プライベート

def _clear_message() -> None:
	global _messages
	_messages = OrderedDict()
	append_message('debug', _print_mode)


def _message_to_stdout() -> None:
	if not _is_favicon():
		_collect()
		p.pprint(_messages)
		_clear_message()


def _messages_to_str() -> None:
	if not _is_favicon():
		_collect()
		pf = p.pformat(_messages)
		_clear_message()
		return pf


def _message_to_http_head(prefix: str) -> OrderedDict:
	if not _is_favicon():
		_collect()
		out_list = _dict_format(_messages, prefix)
		_clear_message()
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
	order_dic = _message_to_http_head('X-DEBUG')
	if order_dic:
		for key_, item_ in order_dic.items():
			res_.headers.append((key_, item_))


def _debug_print_body(res_: Response) -> None:
	str_ = _messages_to_str()
	res_.body += "\n<hr><pre>\n" + str(str_) + "</pre>"


def _is_favicon():
	if settings.environ and settings.environ['PATH_INFO'] == '/favicon.ico':
		return True
	else:
		return False


	#if __name__ == '__main__':
	#res = Response()

	#_clear_message()
	#mode('body')
	#output_message(res)
	#p.pprint(res.body)
	#
	#_clear_message()
	#_print_mode='head'
	#print(_print_mode)
	#output_message(res)
	#p.pprint(res.headers)

	#_clear_message()
	#set_print_mode('true')
	#output_message(res)

	#pass

	# TODO ;debug = context  #CLIならbody webならHeader
	# TODO コード整理する
