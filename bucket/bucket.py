"""
test
"""
import sys

from datetime import datetime

aaa = datetime.utcnow()
tstr = aaa.strftime('%Y%m%d%H%M%S%f')

print(tstr)

sys.exit()


def test_aaaa():
	print('-1:', '-1'.isdecimal())
	print('−１:', '−１'.isdecimal())
	print('-一:', '一'.isdecimal())
	print('1:', '1'.isdecimal())
	print('１:', '１'.isdecimal())
	print('一:', '一'.isdecimal())
	print('1:', '1'.isnumeric())
	print('１:', '１'.isnumeric())
	print('一:', '一'.isnumeric())
	print('1:', '1'.isnumeric())
	print('１:', '１'.isnumeric())
	print('一:', '一'.isnumeric())
	pass


test_aaaa()
exit()

import random

print('ccccddd')


def rnd():
	print('cccc')
	return random.random()


class aaa:
	pass


c = aaa()
c.bbb = 41242

print(c)
print(c.bbb)
print(c.ccc)

b = object()

# b.hogeho = 'aaaaa'
# b.dddd = 3253

print(b)

a = {
	'REMOTE_ADDR': '127.0.0.1',
	'SCRIPT_NAME': '',
	'DISPLAY': '/tmp/launch-HCt8qh/org.x:0',
	'Apple_Ubiquity_Message': '/tmp/launch-5Fwrhw/Apple_Ubiquity_Message',
	'wsgi.multithread': True,
	'SERVER_NAME': 'localhost',
	'SERVER_SOFTWARE': 'WSGIServer/0.2',
	'REQUEST_METHOD': 'GET',
	'SERVER_PROTOCOL': 'HTTP/1.1',
	'SERVER_PORT': '80',
	'Apple_PubSub_Socket_Render': '/tmp/launch-2lM0Oa/Render',
	'PYCHARM_HOSTED': '1',
	'wsgi.file_wrapper': "<class 'wsgiref.util.FileWrapper'>",
	'__PYVENV_LAUNCHER__': '/Library/Frameworks/Python.framework/Versions/3.4/bin/python3',
	'SSH_AUTH_SOCK': '/tmp/launch-a7FFIW/Listeners',
	'COMMAND_MODE': 'unix2003',
	'wsgi.run_once': False,
	'HTTP_CACHE_CONTROL': 'max-age=0',
	'__CF_USER_TEXT_ENCODING': '0x1F5:1:14',
	'GATEWAY_INTERFACE': 'CGI/1.1',
	'TMPDIR': '/var/folders/3s/q4h3sr613kx978hqgr6_jlfc0000gn/T/',
	'HTTP_ACCEPT_LANGUAGE': 'ja,en-US;q=0.8,en;q=0.6',
	'wsgi.errors': "<_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>",
	'wsgi.input': "<_io.BufferedReader name=7>",
	'REMOTE_HOST': '',
	'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36',
	'QUERY_STRING': 'Data.time_line',
	'HTTP_CONNECTION': 'keep-alive',
	'PATH': '/opt/local/bin:/opt/local/sbin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/X11/bin:/usr/local/git/bin:/opt/local/bin:/usr/local/mysql/bin',
	'wsgi.multiprocess': False,
	'HOME': '/Users/user01',
	'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'HTTP_ACCEPT_ENCODING': 'gzip,deflate,sdch',
	'HTTP_HOST': 'localhost:8080',
	'SHELL': '/bin/bash',
	'CONTENT_LENGTH': '',
	'LOGNAME': 'user01',
	'CONTENT_TYPE': 'text/plain',
	'PATH_INFO': '/',
	'wsgi.url_scheme': 'http',
	'PYTHONUNBUFFERED': '1',
	'PYTHONIOENCODING': 'UTF-8',
	'HTTP_DNT': '1',
	'wsgi.version': (1, 0)
}
#
#
#class dichoge():
#	def __init__(self):
#		self.__aaa = 'BBB'
#
#	def func(self):
#		pass
#
#
#obj = dichoge()
#obj.hoge = "aaa"
#print(obj.__dict__)
#print(vars(obj))
#
#exit()
#dicc = {}
#dicc.hoge = 'aaa'
#print(dicc.hoge)
#
#exit()
#
#import sqlite3
#
#con = sqlite3.connect(":memory:")
#sql = """
#create table user (
#  name varchar(10),
#  age integer,
#  address varchar(200)
#);
#"""
#con.execute(sql)
#sql = "insert into user values ('jon', 26, 'USA')"
#con.execute(sql)
#con.executemany("insert into user values (?, ?, ?)",
#                [("takasi", 35, "japan"),
#                 ("guid", 40, "Holland")])
#c = con.cursor()
#c.execute("select * from user")
#for row in c: # rowはtuple
#	print(row[0], row[1], row[2])
#con.close()
#
#exit()
#
#from datetime import datetime
#from myapp.common import settings
#
#
#def count():  # PENDING プラグイン化
#	"""
#	日数カウント
#	"""
#	a = settings.get_ini('count')
#
#	tstr = a['to_time_str']
#	print(tstr)
#	to = datetime.strptime(tstr, '%Y-%m-%d %H:%M:%S')
#	from_ = datetime.now()
#	return to - from_
#
#
#print(count())
#
#
#def cache_class():
#	"""
#	変数キャッシュのテスト
#	"""
#
#	def _aaa():
#		return _aaa
#		pass
#
#	x = _aaa()
#
#	print(x)
#
#	b = {}
#
#
#	class _Bbb():
#		def __init__(self):
#			pass
#
#		def __del__(self):
#			print('dell')
#			del b[id(self)]
#
#		@property
#		def status_code(self):
#			"""
#			test
#			@return:
#			"""
#			obj = b[id(self)]
#			return obj['status_code']
#
#		@status_code.setter
#		def status_code(self, val):
#			"""
#			test
#			@param val:
#			@return:
#			"""
#			#			global b
#			obj = {'status_code': val}
#			b[id(self)] = obj
#
#	print(b)
#	a = _Bbb()
#	a.hoge = 'piyo'
#	a.status_code = 'gggg'
#	print(b)
#	print(vars(a))
#	print(a.status_code)
#	del a
#	print(b)
#
#
#cache_class()
#
#

#
#
#from bucket.importtest import piyo
#
#print(piyo.status_code)
#piyo.status_code = 123
#print(piyo.status_code)
#
#
#def aaa():
#	bbb = 0
#	return bbb
#
#
#aaa.bbb = 1
#
#aaa()

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

