"""
# myapp.common.application
"""
from myapp.common.response import Response
from myapp.common.debug import Debug
from myapp.common import settings


def _controller_dispatcher(module_name, class_name):
	mod = __import__(module_name)
	components = module_name.split('.')
	for c in components[1:]:
		mod = getattr(mod, c)
	return getattr(mod, class_name)


class Application():
	debug = None

	def __init__(self):
		conf = settings.get_ini('application')
		if conf['debug'] == 'true':
			self.debug = Debug()


	def main(self):

		controller = _controller_dispatcher('myapp.controller.data', "Data")
		ccc = controller()

		response = Response()
		response.body = ccc.run()

		self._debug_print()

		return response


	def _debug_print(self):
		if self.debug:
			self.debug.print()
