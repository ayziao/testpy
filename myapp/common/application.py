"""
# myapp.common.application
"""
from myapp.common import settings
from myapp.common import utility
from myapp.common.request import Request
from myapp.common.response import Response

from myapp.common.debug import Debug


def main():
	"""
	# メイン
	"""
	req = _assemble_main_request()  # メインリクエスト取得
	controller_instance = _controller_dispatcher(req.controller_class_name)  # コントローラ取得

	res = Response()  # レスポンス組み立て
	res.body = _run_controller_method(controller_instance, req.method_name)  # コントローラ実行

	_debug_print()

	return res


#プライベート
def _assemble_main_request():
	"""
	# メインリクエスト組み立て
	"""
	req = Request()
	req.controller_class_name = 'Data'  # TODO 環境から取る
	req.method_name = 'run'
	return req


def _controller_dispatcher(class_name):
	"""
	# コントローラ振り分け
	"""
	module_name = 'myapp.controller.' + class_name.lower()
	mod = utility.import_(module_name)

	try:
		class_object = getattr(mod, class_name)
		return class_object()
	except AttributeError:
		# PENDING 404?
		return None


def _run_controller_method(controller, method):
	"""
	# メソッド実行
	"""
	try:
		m = getattr(controller, method)
		return m()
	except AttributeError:
		# PENDING 404?
		return ''


#デバッグ関連
_debug = None


def _debug_setting():
	global _debug
	conf = settings.get_ini('application')
	if conf['debug'] == 'true':
		_debug = Debug()


#TODO HTML内に表示するようにする
def _debug_print():
	if _debug:
		_debug.print()


_debug_setting()
