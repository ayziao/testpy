"""
test
"""
import unittest
from unittest import mock

import bucket

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
		aaa = 'bb {} cc'
		bbb = aaa.format("aaa")
		print(bbb)

	@mock.patch('bucket.random')
	def test_aaa(self, moc):
		print('aaabbb')

		def method():
			return 9

		moc.random = method
		print(bucket.rnd())


if __name__ == '__main__':
	unittest.main()
