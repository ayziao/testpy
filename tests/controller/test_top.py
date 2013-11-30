"""
トップコントローラ単体テスト
"""
import unittest

from myapp.common.request import Request
from myapp.controller.top import Top


class TestTop(unittest.TestCase):
	def test_init(self):
		req = Request()
		cnr = Top(req)
		self.assertIsInstance(cnr, Top)

	def test_run(self):
		req = Request()
		req.extension = 'raw'
		cnr = Top(req)
		ret = cnr.run()
		self.assertEqual(ret.body, 'Hello world! top')



