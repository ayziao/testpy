from myapp.common.Utility import Response
import myapp.common.initializesetting as ini


class Application():
	def main(self):
		response = Response()
		conf = ini.get_ini('section')
		output_str = conf['key']
		output_str += ' Hello world!'
		response.body = output_str
		return response

