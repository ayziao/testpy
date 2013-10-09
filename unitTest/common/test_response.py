import unittest
from myapp.common.response import Response


class TestResponse(unittest.TestCase):
	def test_init(self):
		res = Response()
		self.assertEqual(res.status, '200 OK')


	def test_status_code_404(self):
		res = Response()
		res.status_code = 404
		self.assertEqual(res.status, '404 Not Found')


	def test_status_code_200(self):
		res = Response()
		res.status_code = 200
		self.assertEqual(res.status, '200 OK')


if __name__ == '__main__':
	unittest.main()
