"""
# アプリケーション共通
#
# myapp.common.application
"""
from myapp.common import settings
from myapp.common import utility
from myapp.common import request
from myapp.common import response


def main() -> response.Response:
	"""
	# メイン
	"""
	_debug_setting()

	_assemble_main_request()  # メインリクエスト組み立て
	run()

	res = response.get_instance()

	#TODO エラー処理

	_debug_print()

	return res


def run():
	req = request.get_instance()
	controller_instance = _controller_dispatcher(req.controller_class_name)  # コントローラ取得

	res = response.create_instance()
	res.body = _run_controller_method(controller_instance, req.method_name)  # コントローラ実行


def view_dispatcher(class_name: str) -> "view class":
	"""
	# ビュー振り分け
	@param class_name: クラス名
	"""
	module_name = 'myapp.view.' + class_name.lower()  # PENDING 名前空間を動的に取る？
	mod = utility.import_(module_name)

	try:
		class_object = getattr(mod, class_name)
		return class_object()
	except AttributeError:
		# PENDING 404?
		return None


#プライベート
def _assemble_main_request() -> request.Request:
	"""
	# メインリクエスト組み立て
	"""
	req = request.get_instance()
	req.controller_class_name = 'Data'  # TODO 環境から取る
	req.method_name = 'run'
	return req


def _controller_dispatcher(class_name: str) -> "controller class":
	"""
	# コントローラ振り分け
	@param class_name:
	"""
	module_name = 'myapp.controller.' + class_name.lower()
	mod = utility.import_(module_name)

	try:
		class_object = getattr(mod, class_name)
		return class_object()
	except AttributeError:
		# PENDING 404?
		return None


def _run_controller_method(controller: str, method: str) -> "method":
	"""
	# メソッド実行
	@param controller:
	@param method:
	"""
	try:
		m = getattr(controller, method)
		return m()
	except AttributeError:
		# PENDING 404?
		return ''


#デバッグ関連
_debug = None
#todo debugクラスをmoduleにする

def _debug_setting() -> None:
	global _debug
	conf = settings.get_ini('application')
	if conf['debug'] and conf['debug'] != 'false':
		d = utility.import_('myapp.common.debug')
		d.mode(conf['debug'])
		_debug = d.Debug()

#todo ↓をdebugモジュールに移動する


def _debug_print() -> None:
	if _debug:
		_debug.print()


# TODO ;debug = head  #HTTPHeader
# TODO ;debug = context  #CLIならbody webならHeader


