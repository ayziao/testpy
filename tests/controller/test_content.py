"""
コンテンツコントローラ単体テスト
"""
import unittest
from unittest.mock import patch

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


	@patch('myapp.controller.content.BaseData')
	def test_get_id(self, BaseDataMock):
		instance = BaseDataMock.return_value
		instance.id = '20121231235959123456'
		instance.title = 'title'
		instance.tag = 'tag'
		instance.body = 'the result'
		instance.datetime = 'datetime'

		req = Request()
		req.path = '20121231235959123456'

		obj = Content(req)
		res = obj._get_id()

		BaseDataMock.assert_called_with()
		instance.load_by_id.assert_called_with('20121231235959123456')
		self.assertEqual(res.body, '20121231235959123456 title tag<br>the result<br>datetime')

	@patch('myapp.controller.content.BaseData')
	def test_get_title(self, BaseDataMock):
		instance = BaseDataMock.return_value
		instance.id = '20121231235959123456'
		instance.title = 'title'
		instance.tag = 'tag'
		instance.body = 'the result'
		instance.datetime = 'datetime'

		req = Request()
		req.path = 'title'

		obj = Content(req)
		res = obj._get_title()

		BaseDataMock.assert_called_with()
		instance.load_by_title.assert_called_with('title')
		self.assertEqual(res.body, '20121231235959123456 title tag<br>the result<br>datetime')


class dummy():
	def __init__(self, id):
		self.body = 'dummy'
		print('jhoge')

	def load(self, id):
		pass


if __name__ == '__main__':
	unittest.main()
