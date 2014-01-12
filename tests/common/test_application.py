"""
共通アプリケーション単体テスト
"""
import unittest
from unittest import mock
from unittest.mock import MagicMock

from myapp.common import application
from myapp.common import settings
from myapp.controller.top import Top
from myapp.controller.error import Error
from myapp.common.request import Request


class TestApplication(unittest.TestCase):
	def test_run(self):
		req = Request()
		req.extension = 'raw'
		req.controller_class_name = 'Top'  # PENDING 環境から取る
		req.method_name = 'run'
		res = application.run(req)
		self.assertEqual(res.body, 'Hello world! top')

	@mock.patch('myapp.common.application.database')
	def test_main(self, moc):
		def method():
			pass

		moc.get_connection = method

		ret = application.main_run()
		self.assertEqual(ret.body[0:6], 'Hello ')

	def test_view_dispatcher(self):
		req = Request()
		req.extension = 'raw'
		view_instance = application.view_dispatcher('Top', req)
		res = view_instance.view(None)
		self.assertEqual(res.body, 'Hello world! top')

	def test_view_dispatcher_none(self):
		req = Request()
		view_instance = application.view_dispatcher('none', req)
		self.assertIsNone(view_instance)

	def test_assemble_main_request(self):
		req = application._assemble_main_request()
		self.assertEqual(req.controller_class_name, 'Top')

	def test_assemble_main_request_web(self):
		bk = settings.environ

		settings.environ = {'QUERY_STRING': "data.time_line={'hoge':'piyo'}", 'PATH_INFO': '/'}
		req = Request()
		req = application._assemble_main_request_web(req)
		self.assertEqual(req.controller_class_name, 'data')
		self.assertEqual(req.method_name, 'time_line')

		settings.environ = {'QUERY_STRING': "", 'PATH_INFO': '/'}
		req = Request()
		req = application._assemble_main_request_web(req)
		self.assertEqual(req.controller_class_name, 'Top')
		self.assertEqual(req.method_name, 'run')

		settings.environ = bk

	def test_controller_dispatcher(self):
		req = Request()
		controller_instance = application._controller_dispatcher('Top', req)
		self.assertTrue(isinstance(controller_instance, Top))

	def test_controller_dispatcher_none(self):
		req = Request()
		controller_instance = application._controller_dispatcher('none', req)
		self.assertIsInstance(controller_instance, Error)


	def test_run_controller_method(self):
		with self.assertRaises(AssertionError):
			controller_instance = application._run_controller_method('none', 'none')
			self.assertIsInstance(controller_instance, Error)

	def test_debug_message(self):
		application._debug = MagicMock()
		application.debug_message('test', 'test')
		application._debug = None

	# PENDING カバレッジ上げるためだけ アサーション未定

	def test_debug_print(self):
		application._debug = MagicMock()
		application._debug_print(None)
		application._debug = None

	# PENDING カバレッジ上げるためだけ アサーション未定

	def test_debug_instance_set(self):
		test = {'debug': 'unit test'}
		application._debug_instance_set(test)
		application._debug = None

	# PENDING カバレッジ上げるためだけ アサーション未定


#メインリクエスト取得
#リクエスト組み立て
#リクエストプッシュ
#アプリ実行
#コントローラ選択

if __name__ == '__main__':
	unittest.main()
