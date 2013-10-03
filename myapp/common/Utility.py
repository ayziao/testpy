from pprint import pprint
import configparser


def debug_print(environ):
	if environ['PATH_INFO'] != '/favicon.ico':
		from pprint import pprint

		pprint(environ)


def load_conf():
	conf = configparser.ConfigParser()
	conf.read('../config/setting.ini.sample')
	return conf


class Response():
	status = '200 OK'
	headers = [('Content-Type', 'text/plain; charset=utf-8')]
	body = ''


def pppp():
	pprint(globals())

