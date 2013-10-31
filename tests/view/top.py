import unittest

from myapp.view.top import Top


class TestVewTop(unittest.TestCase):
	def test_something(self):
		top = Top()
		top.viewhtml()
		self.assertEqual(True, False)


if __name__ == '__main__':
	unittest.main()
