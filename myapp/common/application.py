from myapp.common.Utility import Response
from myapp.common.Utility import load_conf


class Application():
	def main(self):
		response = Response()
		conf = load_conf()
		output_str = conf['section']['key']
		output_str += ' Hello world!'
		response.body = output_str
		return response

