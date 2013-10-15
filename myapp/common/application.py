"""
# myapp.common.application
"""
from myapp.common import settings
from myapp.common import utility
from myapp.common.request import Request
from myapp.common.response import Response

from myapp.common.debug import Debug

debug = None

conf = settings.get_ini('application')
if conf['debug'] == 'true':
	debug = Debug()


def main():
	req = _assemble_main_request()
	controller_instance = _controller_dispatcher(req.controller_class_name)

	response = Response()
	response.body = controller_instance.run()

	_debug_print()

	return response


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
		return None


def _assemble_main_request():
	"""
	# メインリクエスト組み立て
	"""
	req = Request()
	req.controller_class_name = 'Data'  # TODO 環境から取る
	req.method_name = 'run'
	return req


#TODO HTML内に表示するようにする
def _debug_print():
	if debug:
		debug.print()
