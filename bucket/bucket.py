import configparser
from pprint import pprint


def hoge():
	return 'piyo'


def pppp():
	pprint(globals())


if __name__ == '__main__':
	conf = configparser.ConfigParser()
	conf.read('conf.ini')
	pprint(conf['aaa']['bbb'])
	pprint(globals())

	exit()

	import sys
	from pprint import pprint

	a = {}
	a['a'] = 2
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
