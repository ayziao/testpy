import unittest
from collections import OrderedDict

from myapp.common import debug


class TestDebug(unittest.TestCase):
	"""
	共通デバッグモジュールのテスト
	"""

	def test_collect(self):
		debug.clear_message()
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
		debug.clear_message()
		debug._collect()
		l = []
		for v in debug.get_message_dic():
			if 'memory' in v:
				l.append('memory')
		self.assertIn('memory', l)
		debug.clear_message()
		l = []
		for v in debug.get_message_dic():
			if 'memory' in v:
				l.append('memory')
		self.assertNotIn('memory', l)

	def test_get_message_dic(self):
		dic = debug.get_message_dic()
		self.assertIsInstance(dic, OrderedDict)

	@unittest.skip("stdout skip")
	def test_message_to_stdout(self):
		# PENDING print関数をラップするべきか
		self.fail("shouldn't happen")
		pass

	def test_message_to_http_head(self):
		heads = debug._message_to_http_head('X-TEST')
		tapl = ('X-TEST-debug', 'False')
		first_head = heads.popitem(False)
		self.assertEqual(first_head, tapl)


if __name__ == '__main__':
	unittest.main()

	# TODO テスト書く