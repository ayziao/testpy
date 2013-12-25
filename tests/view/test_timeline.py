import unittest

from myapp.common.request import Request
from myapp.view.timeline import TimeLine


class TestVewTimeLine(unittest.TestCase):
	def test_view(self):
		req = Request()
		view = TimeLine(req)
		res = view.view(None)
		self.assertEqual(res.body[0:17], "time line")  # PENDING もっとマシに というかViewのテストってどうあるべきなのよ

	def test_view_html(self):
		req = Request()
		view = TimeLine(req)
		dummy.id = '20121231235959123456'
		dummy.tag = 'dummy_tag1 dummy_tag2'
		dummy.title = 'dummy'
		dummy.datetime = '2012-12-31 23:59:59.123456'
		dummy.body = 'dummy body'
		import copy

		d2 = copy.copy(dummy)

		html = view._view_html([dummy, d2])
		self.assertEqual(html[0:17], "<html>\n\t<head>\n\t\t")  # PENDING もっとマシに というかViewのテストってどうあるべきなのよ

	# print(html)


class dummy:
	pass