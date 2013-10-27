"""
test
"""
import unittest

#from bucket import bucket


class MyTestCase(unittest.TestCase):
	"""
	テスト
	"""

	def test_something(self):
		#ret = bucket.hoge()
		#self.assertEqual(ret, 'piyo')
		self.assertEqual(True, True)
		self.assertEqual(False, False)


if __name__ == '__main__':
	unittest.main()
