from myapp.common.Utility import Response
from myapp.common.debug import Debug
import myapp.common.initializesetting as ini


class Application():
	debug = None

	def main(self):
		response = Response()
		conf = ini.get_ini('application')
		if conf['debug'] == 'true':
			self.debug = Debug()
		output_str = 'Hello world!'
		response.body = output_str
		if self.debug:
			self.debug.print()
		return response

