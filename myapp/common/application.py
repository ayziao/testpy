"""
# 共通 アプリケーションモジュール
# myapp.common.application

"""
from myapp.common import settings
from myapp.common import utility
from myapp.common import request
from myapp.common import response


_instance = []


class Application:
	"""
	アプリケーションクラス
	"""

	def __init__(self, req: request.Request):
		self.request = req
		self.response = response.Response()

	def run(self) -> None:
		"""
		実行
		"""
		req = self.request
		controller_instance = _controller_dispatcher(req.controller_class_name, self.request)  # コントローラ取得
		_run_controller_method(controller_instance, req.method_name)  # コントローラ実行


#パブリックメソッド
def get_instance() -> Application:
	"""
	# 最新のスタックを返す
	"""
	return _instance[-1]


def main() -> response.Response:
	"""
	# メイン
	"""
	_debug_setting()

	_instance.clear()
	req = _assemble_main_request()  # メインリクエスト組み立て
	sub(req)
	app = get_instance()
	_instance.clear()

	#PENDING エラー処理

	_debug_print(app.response)

	return app.response


def sub(req):
	app = Application(req)
	_instance.append(app)
	app.run()


def view_dispatcher(class_name: str, aaa) -> "view instance":
	"""
	# ビュー振り分け
	@param class_name: クラス名
	@return ビューインスタンス

	コントローラからビューをnewする方法検討
		ビュー名(画面名) モデル キューは暗黙的
		抽象コントローラにビュー生成メソッド？
		ビューファクトリーをCommonに置く？＞デザパタよく把握してないのでとりあえずディスパッチャって名前でInstance生成するやつ作る
	"""

	module_name = 'myapp.view.' + class_name.lower()  # PENDING 名前空間を動的に取る？
	mod = utility.import_(module_name)

	try:
		class_object = getattr(mod, class_name)
		return class_object(aaa)
	except AttributeError:
		# PENDING 404?
		return None


#プライベート
def _assemble_main_request() -> request.Request:
	"""
	# メインリクエスト組み立て
	"""
	if settings.environ:
		return _assemble_main_request_web()
	else:
		return _assemble_main_request_cli()


def _assemble_main_request_web() -> request.Request:
	req = request.Request()
	req.controller_class_name = 'Top'  # PENDING 環境から取る
	req.method_name = 'run'
	return req


def _assemble_main_request_cli() -> request.Request:
	req = request.Request()
	req.extension = 'raw'  # PENDING 環境から取る
	req.controller_class_name = 'Top'  # PENDING 環境から取る
	req.method_name = 'run'
	return req


def _controller_dispatcher(class_name: str, req) -> "controller instance":
	"""
	# コントローラ振り分け
	@param class_name:
	"""
	module_name = 'myapp.controller.' + class_name.lower()
	mod = utility.import_(module_name)

	try:
		class_object = getattr(mod, class_name)
		return class_object(req)
	except AttributeError:
		# PENDING 404?
		return None


def _run_controller_method(controller: "controller instance", method: str) -> None:
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
		return None


#デバッグ関連
_debug = None


def debug_message(name: str, obj) -> None:
	"""
	デバッグメッセージ追加
	@param name: 名称
	@param obj: なんでも
	"""
	if _debug:
		_debug.append_message(name, obj)


def _debug_setting() -> None:
	conf = settings.get_ini('application')
	if conf['debug'] and conf['debug'] != 'false':
		_debug_instance_set(conf)


def _debug_instance_set(conf):
	global _debug
	_debug = utility.import_('myapp.common.debug')
	_debug.set_print_mode(conf['debug'])


def _debug_print(res) -> None:
	if _debug:
		_debug.output_message(res)


#
#def create_instance() -> Request:
#	"""
#	# 新しくスタック積んで返す
#	"""
#	_instance.append(Request())
#
#	return _instance[-1]
#
#
#def get_instance() -> Request:
#	"""
#	# 最新のスタックを返す 空なら作る
#	"""
#	if not _instance:
#		return create_instance()
#	else:
#		return _instance[-1]
#
#
#def pop_instance() -> Request:
#	"""
#	# 最新のスタックを取り出して返す
#	"""
#	if _instance:
#		return _instance.pop()
#	else:
#		return None
