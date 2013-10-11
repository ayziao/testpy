import unittest

from myapp.common import application
from myapp.common.request import Request


class TestApplication(unittest.TestCase):
	#def test_init(self):
	#	#app = Application()
	#	self.assertEqual(application.debug, None)


	def test_main(self):
		#app = Application()
		ret = application.main()
		self.assertEqual(ret.body, 'Hello world!')


	def test_assemble_request(self):
		#app = Application()
		application.assemble_request()
		req = Request()
		self.assertEqual(req.extension, 'test')

#メインリクエスト取得
#リクエスト組み立て
#リクエストプッシュ
#アプリ実行
#コントローラ選択

if __name__ == '__main__':
	unittest.main()



	#TODO ;debug = head  #HTTPHeader
	#TODO ;debug = body  #ボディ内