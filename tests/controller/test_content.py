"""
コンテンツコントローラ単体テスト
"""
import unittest
from unittest import mock

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

		obj._get_id = get_id

		self.assertTrue(obj.run())

	def test_run_title(self):
		req = Request()
		req.path = 'title'
		obj = Content(req)

		#分岐調べるだけなので分岐先すげ替える
		def get_title():
			return True

		obj._get_title = get_title

		self.assertTrue(obj.run())

	def test_run_top(self):
		req = Request()
		req.path = ''
		obj = Content(req)

		#分岐調べるだけなので分岐先すげ替える
		def moc():
			return True

		obj._get_top = moc

		self.assertTrue(obj.run())


	@mock.patch('myapp.model.basedata.BaseData')
	def test_get_id(self, moc):
		moc = dummy
		req = Request()
		req.path = '20121231235959123456'
		obj = Content(req)
		res = obj._get_id()

	#self.assertEqual(res.body, '')


class dummy():
	def __init__(self, id):
		self.body = 'dummy'
		print('jhoge')

	def load(self, id):
		pass


if __name__ == '__main__':
	unittest.main()
