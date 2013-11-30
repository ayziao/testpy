import unittest

from myapp.common.request import Request
from myapp.view.timeline import TimeLine


class TestVewTimeline(unittest.TestCase):
	def test_view(self):
		req = Request()
		view = TimeLine(req)
		html = view._view_html(None)
		self.assertEqual(html[0:17], "<html>\n\t<head>\n\t\t") # TODO もっとマシに
		pass