"""
トップコントローラ単体テスト
"""
import unittest
from unittest.mock import MagicMock

from myapp.common.request import Request
from myapp.controller.top import Top


class TestData(unittest.TestCase):
	def test_init(self):
		obj = MagicMock
		obj.title = ''
		cnr = Top(obj)
		self.assertIsInstance(cnr, Top)

	def test_run(self):
		req = Request()
		req.extension = 'raw'
		cnr = Top(req)
		ret = cnr.run()
		self.assertEqual(ret.body, 'Hello world!')



