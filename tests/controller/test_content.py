"""
コンテンツコントローラ単体テスト
"""
import unittest

from myapp.controller.content import Content
from myapp.common.request import Request


class TestContent(unittest.TestCase):
	def test_init(self):
		req = Request()
		req.path = 'TestContent_test_init'
		obj = Content(req)
		self.assertEqual(type(obj), Content)

	def test_run_id(self):
		req = Request()
		req.path = '20140101235959123456'
		obj = Content(req)

		#分岐調べるだけなので分岐先すげ替える
		def get_id():
			return True

		obj.get_id = get_id

		self.assertTrue(obj.run())


	def test_aaaa(self):
		# print('-1:', '-1'.isdecimal())
		# print('−１:', '−１'.isdecimal())
		# print('-一:','一'.isdecimal())
		# print('1:', '1'.isdecimal())
		# print('１:', '１'.isdecimal())
		# print('一:','一'.isdecimal())
		# print('1:', '1'.isnumeric())
		# print('１:', '１'.isnumeric())
		# print('一:','一'.isnumeric())
		# print('1:', '1'.isnumeric())
		# print('１:', '１'.isnumeric())
		# print('一:','一'.isnumeric())
		pass


if __name__ == '__main__':
	unittest.main()
