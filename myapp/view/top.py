"""
# myapp.view.top
"""
# TODO投稿フォーム
from xml.dom import minidom
from myapp.common import application


class Top:
	"""
	トップページ
	"""

	def view(self):
		"""
		表示

		形式によって出し分ける
		"""
		req = application.get_instance().request
		if (req.extension == 'html'):
			self._viewhtml()
		#if (req.Request.extension == 'json'):
		#	pass
		else:
			return 'Hello world!'

	def _viewhtml(self):
		title = "titlあああ"  # PENDING タイトル
		body = "はろー"
		#form = self.form()
		html = """
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html charset=UTF-8" />
		<title>%s</title>
	</head>
	<body>
		<p>%s</p>
	</body>
</html>
""" % (title, body)

		doc = minidom.parseString(html.replace("\t", "").replace("\n", ''))
		#header("Content-Type: text/html charset=UTF-8")
		return doc

