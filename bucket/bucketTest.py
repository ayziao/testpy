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

	#@unittest.skip("demonstrating skipping")
	def test_hoge(self):
		aaa = 'bb %s cc'
		bbb = aaa % "aaa"
		print(bbb)


if __name__ == '__main__':
	unittest.main()
