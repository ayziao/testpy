import unittest
from unittest import mock
from datetime import datetime

from myapp.common.request import Request
from myapp.controller.data import Data


class TestData(unittest.TestCase):
	"""
	データコントローラ単体テスト
	"""

	def test_init(self):
		req = Request()
		data = Data(req)
		self.assertIsInstance(data, Data)

	def test_run(self):
		req = Request()
		data = Data(req)
		data.run()
		self.assertTrue(True)  # PENDING アサ

	@mock.patch('myapp.controller.data.BaseData')
	def test_post(self, moc):
		instance = moc.return_value # mockのreturn_valueはデフォルトでモックのインスタンスになってるので受け取ってごにょごにょする

		def method():
			self.assertTrue(True)

		instance.save_as = method
		moc.commit = method

		req = Request()
		req.parameter = {'title':['test title'], 'tag':['test tag'], 'body':['test body']}
		req.datetime = datetime.utcnow()

		data = Data(req)

		res = data.post()

		self.assertEqual(res.body, 'post')


	@mock.patch('myapp.controller.data.BaseData')
	def test_time_line(self, moc):
		def method():
			dummy.id = '20121231235959123456'
			dummy.tag = 'dummy_tag1 dummy_tag2'
			dummy.title = 'dummy'
			dummy.datetime = '2012-12-31 23:59:59.123456'
			dummy.body = 'dummy body'

			return [dummy]

		moc.load_list = method

		req = Request()
		data = Data(req)

		res = data.time_line()
		self.assertEqual(res.body, 'time line')

		req = Request()
		req.extension = 'html'
		req.datetime = datetime.utcnow()
		data = Data(req)

		res = data.time_line()

	# print(res.body)
	#
	# 		self.assertEqual(res.body,
	# 		                 """<html>
	# 	<head>
	# 		<meta content="text/html charset=UTF-8" http-equiv="Content-Type"/>
	# 		<title>タイムライン</title>
	# 	</head>
	# 	<body>
	# 		<div>0 20121231235959123456 dummy dummy_tag1 dummy_tag2 dummy body 2012-12-31 23:59:59.123456</div>
	# 	</body>
	# </html>
	# """)

	# PENDING アサート


class dummy:
	pass