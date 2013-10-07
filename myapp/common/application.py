"""
# myapp.common.application
"""
from myapp.common.response import Response
from myapp.common.debug import Debug
from myapp.common import settings


class Application():
	debug = None

	def __init__(self):
		conf = settings.get_ini('application')
		if conf['debug'] == 'true':
			self.debug = Debug()


	def main(self):

		def my_import(module, class_):
			mod = __import__(module)
			components = module.split('.')
			for c in components[1:]:
				mod = getattr(mod, c)
			return getattr(mod, class_)

		class_ = my_import('myapp.controller.data', "Data")
		ccc = class_()

		response = Response()
		response.body = ccc.run()

		self._debug_print()

		return response


	def _debug_print(self):
		if self.debug:
			self.debug.print()
