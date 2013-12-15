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
			res.body = 'Hello world! {top}'.format(top='top')

		return res

	def _view_html(self):
		_title = "たいとる"  # PENDING タイトル
		_body = "はろー"  # PENDING タイムライン取る 将来的にはユーザが任意の機能を設定できるように
		#form = self.form()  # PENDING 投稿フォーム
		html = _html().strip().format(title=_title, body=_body)

		doc = minidom.parseString(html.replace("\t", "").replace("\n", ''))
		#header("Content-Type: text/html charset=UTF-8")  ＃ PENDING ヘッダ
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
		<p><a href="/?Data.time_line">data time line</a></p>
		<p>
			<a href="/?Account.logout">logout</a><br/>
			<a href="/?Account.signup">signup</a><br/>
			<a href="/?Account.login">login</a><br/>
		</p>
	</body>
</html>
""" #fixME アカウント周り
	return html_str
