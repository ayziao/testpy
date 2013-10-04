import configparser
from datetime import datetime

mypath = ''
start_time = datetime.utcnow()


def set_mypath(str):
	global mypath
	mypath = str


def set_start_time(datetime_):
	global start_time
	start_time = datetime_


def debug_print(environ):
	from pprint import pprint

	if environ['PATH_INFO'] != '/favicon.ico':
		pprint(environ)

		now = datetime.utcnow()
		dif = now - start_time
		pprint(start_time)
		pprint(now)
		pprint(dif)

	if environ['debug'] == True:
		now = datetime.utcnow()
		dif = now - start_time
		pprint(start_time)
		pprint(now)
		pprint(dif)


def load_conf():
	conf = configparser.ConfigParser()
	conf.read(mypath + 'config/setting.ini.sample')
	return conf


class Response():
	status = '200 OK'
	headers = [('Content-Type', 'text/plain; charset=utf-8')]
	body = ''

