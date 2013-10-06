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
		response = Response()
		response.body = 'Hello world!'

		self._debug_print()

		return response


	def _debug_print(self):
		if self.debug:
			self.debug.print()


