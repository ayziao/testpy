"""
データコントローラ単体テスト
"""
import unittest

from myapp.common import request
from myapp.common import application
from myapp.controller.data import Data


class TestData(unittest.TestCase):
	def test_init(self):
		data = Data()
		self.assertIsInstance(data, Data)

	def test_run(self):
		req = request.Request()
		app = application.Application(req)
		application._instance.append(app)
		data = Data()
		data.run()
		self.assertTrue(True)

	# PENDING アサート


