import unittest
from myapp.common.request import Request


class TestRequest(unittest.TestCase):
	"""
	 リクエストクラス単体テスト
	"""

	def test_init(self):
		res = Request()
		self.assertEqual(res.extension, 'html')

#PENDING 値のセットをApplicationでやるか自分で集めてくるか

if __name__ == '__main__':
	unittest.main()