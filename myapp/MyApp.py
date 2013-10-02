#from pprint import pprint
from wsgiref import simple_server

#import common.Utility


def application(environ, start_response):
	start_response('200 OK', [('Content-type', 'text/plain')])
	return 'Hello world'


#def run(app):
#	server = simple_server.make_server('', 8080, app)
#	server.serve_forever()


if __name__ == '__main__':
	#server = simple_server.make_server('localhost', 8080, application)
	server = simple_server.make_server('', 8080, application)
	server.serve_forever()
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
