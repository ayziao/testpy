from datetime import datetime

start_time = datetime.utcnow()
environ = {}

#TODO それぞれクラス作って移動する


def count(self):  # PENDING プラグイン化
	tstr = '2013-10-06 23:59:59'  # TODO 設定ファイルからとる
	from_ = datetime.strptime(tstr, '%Y-%m-%d %H:%M:%S')
	to = datetime.now()
	count = from_ - to
	return count


def set_start_time(datetime_):
	global start_time
	start_time = datetime_


def set_environ(environ_):
	global environ
	environ = environ_


def debug_print(environ):
	from pprint import pprint

	if environ['PATH_INFO'] != '/favicon.ico':
		pprint(environ)

		now = datetime.utcnow()
		dif = now - start_time
		pprint(start_time)
		pprint(now)
		pprint(dif)

	if environ.get('debug') and environ['debug']:
		now = datetime.utcnow()
		dif = now - start_time
		pprint(start_time)
		pprint(now)
		pprint(dif)


class Response():
	status = '200 OK'
	headers = [('Content-Type', 'text/plain; charset=utf-8')]
	body = ''

