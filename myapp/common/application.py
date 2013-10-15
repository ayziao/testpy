"""
# myapp.common.application
"""
from myapp.common.response import Response
from myapp.common.debug import Debug
from myapp.common import settings
from myapp.common import utility

debug = None


def _controller_dispatcher(module_name, class_name):
	mod = utility.import_(module_name)
	return getattr(mod, class_name)


conf = settings.get_ini('application')
if conf['debug'] == 'true':
	debug = Debug()


def main():
	controller = _controller_dispatcher('myapp.controller.data', "Data")
	ccc = controller()

	response = Response()
	response.body = ccc.run()

	_debug_print()

	return response


def assemble_request():
	pass


#TODO HTML内に表示するようにする
def _debug_print():
	if debug:
		debug.print()
