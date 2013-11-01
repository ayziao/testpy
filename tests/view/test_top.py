import unittest

from myapp.view.top import Top

class TestVewTop(unittest.TestCase):
	#@unittest.skip("demonstrating skipping")
	def test_viewhtml(self):
		top = Top()
		doc = top.viewhtml()
		str = doc.toprettyxml()[23:]
		test = "<html>\n\t<head>"
		self.assertEqual(str[0:14], test)


if __name__ == '__main__':
	unittest.main()
