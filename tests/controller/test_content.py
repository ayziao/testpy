"""
コンテンツコントローラ単体テスト
"""
import unittest

from myapp.controller.content import Content


class TestContent(unittest.TestCase):
	def test_init(self):
		obj = Content()
		self.assertEqual(type(obj), Content)


if __name__ == '__main__':
	unittest.main()
