"""
# myapp.view.top
"""
# TODO投稿フォーム
from xml.dom import minidom
from myapp.common.request import Request
from myapp.common.response import Response


class Top:
	"""
	トップページ
	"""

	def __init__(self, req: Request):
		self.request = req

	def view(self, model):
		"""
		表示
		形式によって出し分ける
		@param model: モデルインスタンス
		"""
		tmp = model
		res = Response()
		if self.request.extension == 'html':
			res.body = self._view_html()
		#if (req.Request.extension == 'json'):
		#	pass
		else:
			res.body = 'Hello world!'

		return res

	def _view_html(self):
		title = "たいとる"  # PENDING タイトル
		body = "はろー"
		#form = self.form()
		html = _html()
		html.format(title=title, body=body)

		doc = minidom.parseString(html.replace("\t", "").replace("\n", ''))
		#header("Content-Type: text/html charset=UTF-8")
		return doc.toprettyxml()[23:] # XML宣言削除

	# PENDING HTMLバージョンいくつ宣言にする？


def _html():
	html_str = """
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html charset=UTF-8" />
		<title>{title}</title>
	</head>
	<body>
		<p>{body}</p>
		<p><a href="/?data.time_line">data time line</a></p>
	</body>
</html>
"""
	return html_str
