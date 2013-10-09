import unittest
from myapp.common.request import Request


class TestRequest(unittest.TestCase):
	"""
	 リクエストクラス単体テスト
	"""

	def test_init(self):
		res = Request()
		self.assertEqual(res.extension, 'html')


if __name__ == '__main__':
	unittest.main()