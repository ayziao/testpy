import configparser
from datetime import datetime
from pprint import pprint
from common import settings

print(sys.path)
#path = os.path.dirname(os.path.abspath(__file__)) + '/../'

pprint(globals())


def hoge():
	return 'piyo'


def pppp():
	pprint(globals())


if __name__ == '__main__':
	ini = configparser.ConfigParser()
	ini.read('ini.ini')
	pprint(ini['aaa']['bbb'])
	pprint(globals())

	exit()

	import sys
	from pprint import pprint

	a = {'a': 2}
	m = a.get('b')
	n = None
	pprint(a)
	pprint(globals())
	# pprint(locals())

	pprint(dir())

	pprint(sys.path)
#stdout = StringIO()
#print("Hello world!", file=stdout)
#print(file=stdout)
#h = sorted(environ.items())
#for k, v in h:
#	print(k, '=', repr(v), file=stdout)
#return [stdout.getvalue().encode("utf-8")]

#start_response('200 OK', [('Content-type', 'text/plain')])
#	return 'a'

#return 'Hello world'

#g = globals().copy()
#del g['__builtins__']
#pprint(g)

#def run(app):
#	server = simple_server.make_server('', 8080, app)
#	server.serve_forever()
#run(application)




#x = common.Utility


#def ppp():
#	common.Utility.pppp()
#	pprint(globals())
#
#
#def hello(environ, start_response):
#	u'''
#	Hello, world
#	'''
#
#	#
#	start_response('200 OK', [('Content-Type', 'text/plain')])
#
#	#
#	return ['Hello, World']
#
#

#ppp()
def debug_print(environ_):
	if environ_.get('debug') and environ_['debug']:
		now = datetime.utcnow()
		dif = now - settings.start_time
		pprint(settings.start_time)
		pprint(now)
		pprint(dif)