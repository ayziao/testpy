import configparser
from wsgiref import simple_server


def load_conf():
	conf = configparser.ConfigParser()
	conf.read('../config/setting.ini.sample')
	return conf


def debug_print(environ):
	if environ['PATH_INFO'] != '/favicon.ico':
		from pprint import pprint

		pprint(environ)


def application(environ, start_response):
	debug_print(environ)

	conf = load_conf()
	output_str = conf['section']['key']
	output_str += " Hello world!"

	start_response("200 OK", [('Content-Type', 'text/plain; charset=utf-8')])
	return [output_str.encode("utf-8")]


def main():
	server = simple_server.make_server('', 8080, application)
	server.serve_forever()


if __name__ == '__main__':
	main()

