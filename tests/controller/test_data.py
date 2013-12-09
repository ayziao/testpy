"""
データコントローラ単体テスト
"""
import unittest
from unittest import mock

from myapp.common.request import Request
from myapp.controller.data import Data


class TestData(unittest.TestCase):
	def test_init(self):
		req = Request()
		data = Data(req)
		self.assertIsInstance(data, Data)

	def test_run(self):
		req = Request()
		data = Data(req)
		data.run()
		self.assertTrue(True)  # PENDING アサート


	@mock.patch('myapp.controller.data.BaseData')
	def test_time_line(self, moc):
		def method():
			return [{'_key':'id', 'tag':'dummy_tag1 dummy_tag2', 'title':'dummy', 'datetime':'2012-12-31 23:59:59.123456',
			         'body':'dummy body', 'id':'20121231235959123456'}]

		moc.load_list = method

		req = Request()
		data = Data(req)

		res = data.time_line()

	# print(res.body)

	# PENDING アサート

