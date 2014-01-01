"""
コンテンツコントローラ単体テスト
"""
import unittest

from myapp.controller.content import Content


class MyTestCase(unittest.TestCase):
	def test_something(self):
		obj = Content()
		self.assertEqual(type(obj), Content)


if __name__ == '__main__':
	unittest.main()
