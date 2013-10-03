import configparser
from pprint import pprint
from wsgiref import simple_server

#import common.Utility


def application(environ, start_response):
	conf = configparser.ConfigParser()
	conf.read('../config/setting.ini.sample')

	str = conf['section']['key']

	start_response("200 OK", [('Content-Type', 'text/plain; charset=utf-8')])
	if environ['PATH_INFO'] != '/favicon.ico':
		pprint(environ)

	str += " Hello world!"
	return [str.encode("utf-8")]


if __name__ == '__main__':
	#server = simple_server.make_server('localhost', 8080, application)
	server = simple_server.make_server('', 8080, application)
	server.serve_forever()

