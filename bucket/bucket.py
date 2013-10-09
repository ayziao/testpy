from datetime import datetime


def count():  # PENDING プラグイン化
	tstr = '2013-10-06 23:59:59'  # TODO 設定ファイルからとる
	from_ = datetime.strptime(tstr, '%Y-%m-%d %H:%M:%S')
	to = datetime.now()
	return from_ - to

#def test_application(self):
#	def st(aaa, bbb):
#		pass
#
#	env = {'PATH_INFO': '/favicon.ico', 'debug': False}
#	ret = application(env, st)
#	self.assertEqual(ret, [top_body.encode("utf-8")])

#m = __import__('myapp.controller.data')
#m = __import__('myapp.controller.data')
#mod = __import__('sys', {}, {}, [])


#mod = __import__('myapp.controller', globals(), locals(), ['data'], 0)
#print(data)
#print(dir(data))
#Data = data.Data
#clas = getattr(data,"Data")
#ccc = clas()
#print(ccc)
#ddd = Data()
#print(ddd)
#print(dir(m.controller.data))
#print(dir(mod))
#d = mod.data.Data()
#print(d)

#i = m.controller.data.Data()
#i = m.data.Data()
#i = m.Data()
#print(i.aaa())

#m.controller.data.myfunc()

#def hoge():
#	return 'piyo'
#
#
#def pppp():
#	pprint(globals())
#
#
#if __name__ == '__main__':
#
#	exit()
#
#	import sys
#	from pprint import pprint
#
#	a = {'a': 2}
#	m = a.get('b')
#	n = None
#	pprint(a)
#	pprint(globals())
#	# pprint(locals())
#
#	pprint(dir())
#
#	pprint(sys.path)
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

