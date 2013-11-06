import unittest

from myapp.view.top import Top
from myapp.common.request import Request


class TestVewTop(unittest.TestCase):
	def test_view(self):
		req = Request()

		req.extension = 'html'
		viw = Top(req)
		res = viw.view(None)
		self.assert_html(res.body)

		req.extension = 'raw'
		viw = Top(req)
		res = viw.view(req)
		self.assertEqual(res.body, 'Hello world!')

	def test_view_html(self):
		top = Top(None)
		_str = top._view_html()
		self.assert_html(_str)

	def assert_html(self, _str):
		test = "<html>\n\t<head>"
		self.assertEqual(_str[0:14], test)


if __name__ == '__main__':
	unittest.main()
