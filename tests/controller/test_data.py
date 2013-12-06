"""
データコントローラ単体テスト
"""
import unittest

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
		self.assertTrue(True)
	# PENDING アサート

	def test_time_line(self):
		req = Request()
		data = Data(req)
		res = data.time_line()

	# print(res.body)

	# PENDING アサート

