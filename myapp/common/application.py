"""
# 共通 アプリケーションモジュール
# myapp.common.application

リクエスト解析してコントローラ呼ぶ
pathがあるならコンテンツ
	pathをデータコントローラに投げてデータモデルを受け取る
	コマンドない場合はたんなる表示
コマンドがあればコマンドを実行
	データモデル有りのコマンド
	データモデル無しのコマンド

"""
from myapp.common import settings
from myapp.common import utility
from myapp.common import debug
from myapp.common.request import Request
from myapp.common.response import Response

_instance = []


def main() -> Response:
	"""
	# メイン
	"""
	_debug_setting()

	req = _assemble_main_request()  # メインリクエスト組み立て
	res = run(req)

	#PENDING エラー処理

	_debug_print(res)

	return res


def run(req: Request) -> None:
	"""
	実行
	@param req:
	"""
	controller_instance = _controller_dispatcher(req.controller_class_name, req)  # コントローラ取得
	return _run_controller_method(controller_instance, req.method_name)  # コントローラ実行


def view_dispatcher(class_name: str, req: Request) -> "view instance":
	"""
	# ビュー振り分け
	@param class_name: クラス名
	@param req: リクエストインスタンス
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
		debug_message('view', class_object.__name__)
		return class_object(req)
	except AttributeError:
		# PENDING 404?
		return None


#プライベート
def _assemble_main_request() -> Request:
	"""
	# メインリクエスト組み立て
	"""
	if settings.environ:
		return _assemble_main_request_web()
	else:
		return _assemble_main_request_cli()


def _assemble_main_request_web() -> Request:
	class_name = 'Top'
	method_name = 'run'
	try:
		que = settings.environ['QUERY_STRING']
		ques = que.split('=')
		mmm = ques[0].split('.')
		if len(mmm) > 1:
			class_name = mmm[0]
		if len(mmm) == 2:
			method_name = mmm[1]

	except (AttributeError, KeyError):
		pass

	req = Request()
	req.extension = 'html'  # PENDING 環境から取る
	req.controller_class_name = class_name  # PENDING 環境から取る
	req.method_name = method_name
	return req


def _assemble_main_request_cli() -> Request:
	req = Request()
	req.extension = 'raw'  # PENDING 環境から取る
	req.controller_class_name = 'Top'  # PENDING 環境から取る
	req.method_name = 'run'
	return req


def _controller_dispatcher(class_name: str, req: Request) -> "controller instance":
	"""
	# コントローラ振り分け
	@param class_name:
	"""
	module_name = 'myapp.controller.' + class_name.lower()
	mod = utility.import_(module_name)

	try:
		class_object = getattr(mod, class_name)
		debug_message('controller', class_object.__name__)
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


def _get_debug_obj() -> debug:
	if _debug:
		return _debug


def debug_message(name: str, obj) -> None:
	"""
	デバッグメッセージ追加
	@param name: 名称
	@param obj: なんでも
	"""
	de = _get_debug_obj()
	if de:
		_debug.append_message(name, obj)


def _debug_setting() -> None:
	conf = settings.get_ini('application')
	if conf['debug'] and conf['debug'] != 'false':
		_debug_instance_set(conf)


def _debug_instance_set(conf) -> None:
	global _debug
	#_debug = utility.import_('myapp.common.debug') # PENDING
	_debug = debug
	_debug.set_print_mode(conf['debug'])


def _debug_print(res) -> None:
	de = _get_debug_obj()
	if de:
		de.output_message(res)
