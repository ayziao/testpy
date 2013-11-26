"""
共通レスポンス単体テスト
"""
import unittest
from myapp.common import response


class TestResponse(unittest.TestCase):
	def test_init(self):
		res = response.Response()
		self.assertEqual(res.status_code, 0)
		self.assertEqual(res.status, '200 OK')  # PENDING デフォルト値どうしましょう

	def test_status_code_404(self):
		res = response.Response()
		res.status_code = 404
		self.assertEqual(res.status, '404 Not Found')
		self.assertEqual(res.status_code, 404)

	def test_status_code_200(self):
		res = response.Response()
		res.status_code = 200
		self.assertEqual(res.status, '200 OK')
		self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
	unittest.main()
