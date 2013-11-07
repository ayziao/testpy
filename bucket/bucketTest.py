"""
test
"""
import unittest
from unittest import mock
import importtest.test

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

	@mock.patch('importtest.test.random')
	def test_aaa(self, mmm):
		def method():
			return 9

		mmm.random = method
		print(importtest.test.rnd())


if __name__ == '__main__':
	unittest.main()
