"""
# myapp.view.timeline
"""
# TODO投稿フォーム
from xml.dom import minidom
from myapp.common.request import Request
from myapp.common.response import Response


class TimeLine:
	"""
	タイムライン
	"""

	def __init__(self, req: Request):
		self.request = req

	def view(self, model):
		res = Response()
		if self.request.extension == 'html':
			res.body = self._view_html(model)
		#if (req.Request.extension == 'json'):
		#	pass
		else:
			res.body = 'time line'

		return res

	def _view_html(self, model):
		title = "タイムライン"  # PENDING タイトル
		body = self.body()
		#form = self.form()
		html = _html().format(title=title, body=body)

		doc = minidom.parseString(html.replace("\t", "").replace("\n", ''))
		#header("Content-Type: text/html charset=UTF-8")
		return doc.toprettyxml()[23:] # XML宣言削除

	# PENDING HTMLバージョンいくつ宣言にする？

	def body(self):
		return 'body'


def _html():
	html_str = """
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html charset=UTF-8" />
		<title>{title}</title>
	</head>
	<body>
		{body}
	</body>
</html>
"""
	return html_str
