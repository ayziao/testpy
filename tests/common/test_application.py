"""
共通アプリケーション単体テスト
"""
import unittest

from myapp.common import application
from myapp.controller.data import Data


class TestApplication(unittest.TestCase):
	def test_main(self):
		ret = application.main()
		self.assertEqual(ret.body, 'Hello world!')

	def test_view_dispatcher(self):
		view_instance = application.view_dispatcher('Hello')
		ret = view_instance.view()
		self.assertEqual(ret, 'Hello world!')

	def test_view_dispatcher_none(self):
		view_instance = application.view_dispatcher('none')
		self.assertIsNone(view_instance)

	def test_assemble_main_request(self):
		req = application._assemble_main_request()
		self.assertEqual(req.controller_class_name, 'Data')

	def test_controller_dispatcher(self):
		controller_instance = application._controller_dispatcher('Data')
		self.assertTrue(isinstance(controller_instance, Data))

	def test_controller_dispatcher_none(self):
		controller_instance = application._controller_dispatcher('none')
		self.assertIsNone(controller_instance)

#メインリクエスト取得
#リクエスト組み立て
#リクエストプッシュ
#アプリ実行
#コントローラ選択

if __name__ == '__main__':
	unittest.main()


