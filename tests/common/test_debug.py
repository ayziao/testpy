import unittest
import sys
from collections import OrderedDict

from myapp.common import debug
from myapp.common import response
from myapp.common import settings


class TestDebug(unittest.TestCase):
	"""
	共通デバッグモジュールのテスト
	"""

	def test_collect(self):
		env = {'PATH_INFO': '/favicon.ico'}
		settings.environ = env
		debug._clear_message()
		debug._collect()
		settings.environ = None

		debug._clear_message()
		debug._collect()
		l = []
		for v in debug.get_message_dic():
			if 'memory' in v:
				l.append('memory')
			if 'start_time' in v:
				l.append('start_time')
			if 'end_time' in v:
				l.append('end_time')
			if 'dif' in v:
				l.append('dif')

		self.assertIn('memory', l)
		self.assertIn('start_time', l)
		self.assertIn('end_time', l)
		self.assertIn('dif', l)

	def test_clear_message(self):
		debug._clear_message()
		debug._collect()
		l = []
		for v in debug.get_message_dic():
			if 'memory' in v:
				l.append('memory')
		self.assertIn('memory', l)
		debug._clear_message()
		l = []
		for v in debug.get_message_dic():
			if 'memory' in v:
				l.append('memory')
		self.assertNotIn('memory', l)

	def test_get_message_dic(self):
		dic = debug.get_message_dic()
		self.assertIsInstance(dic, OrderedDict)

	def test_message_to_stdout(self):
		op = Output()
		sys.stdout = op
		debug._message_to_stdout()
		sys.stdout = sys.__stdout__
		test = "{'debug': "
		self.assertEqual(op.pp()[0:10], test)

	def test_message_to_stdout_env_favicon(self):
		env = {'PATH_INFO': '/favicon.ico'}
		settings.environ = env
		op = Output()
		sys.stdout = op
		debug._message_to_stdout()
		sys.stdout = sys.__stdout__
		settings.environ = None
		self.assertEqual(op.pp(), '')


	def test_message_to_http_head(self):
		debug.set_print_mode('head')
		heads = debug._message_to_http_head('X-TEST')
		test_head = ('X-TEST-debug', "'head'")
		first_head = heads.popitem(False)
		self.assertEqual(first_head, test_head)

	def test_debug_print_body(self):
		res = response.Response()
		debug.set_print_mode('body')
		debug._debug_print_body(res)
		test = "\n<hr><pre>\n{'debug': 'body',"
		self.assertEqual(res.body[0:28], test)
		pass

	def test_output_message_head(self):
		res = response.Response()
		debug.set_print_mode('head')
		debug.output_message(res)
		test = ('X-DEBUG-debug', "'head'")
		self.assertEqual(res.headers[1], test)

	def test_output_message_body(self):
		res = response.Response()
		debug.set_print_mode('body')
		debug.output_message(res)
		test = "\n<hr><pre>\n{'debug': 'body',"
		#test = "{'debug': 'body',"
		self.assertEqual(res.body[0:28], test)

	def test_output_message(self):
		res = response.Response()
		debug.set_print_mode('true')
		op = Output()
		sys.stdout = op
		debug.output_message(res)
		sys.stdout = sys.__stdout__
		test = "{'debug': 'true'"
		self.assertEqual(op.pp()[0:16], test)


#PENDING テスト用のutilityつくる？ common.utilityに入れる？
#PENDING というかもっといい方法がありそうな 標準出力を奪うの
class Output():
	def __init__(self):
		self.str = ''

	def write(self, val):
		self.str += val

	def close(self):
		return 0

	def flush(self):
		return 0

	def pp(self):
		return self.str


if __name__ == '__main__':
	unittest.main()
