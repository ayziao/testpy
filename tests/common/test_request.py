"""
共通リクエスト単体テスト
"""
import unittest
from myapp.common import request


class TestRequest(unittest.TestCase):
	"""
	リクエストクラス単体テスト
	"""

	def test_init(self):
		res = request.Request()
		self.assertEqual(res.extension, 'html')

	#
	#def test_create_instance(self):
	#	res = request.create_instance()
	#	self.assertEqual(res.extension, 'html')
	#
	#
	#def test_pop_instance(self):
	#	res = request.pop_instance()
	#	self.assertEqual(res.extension, 'html')
	#	request.pop_instance()
	#	request.pop_instance()
	#	request.pop_instance()
	#	request.pop_instance()
	#	request.pop_instance()
	#	res = request.pop_instance()
	#	# PENDING 全消去メソッド作っとく？
	#	self.assertIsNone(res)

#PENDING 値のセットをApplicationでやるか自分で集めてくるか

if __name__ == '__main__':
	unittest.main()
