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

	def view(self, model_list):
		res = Response()
		if self.request.extension == 'html':
			res.body = self._view_html(model_list)
		#if (req.Request.extension == 'json'):
		#	pass
		else:
			res.body = 'time line'

		return res

	def _view_html(self, model_list):
		title = "タイムライン"  # PENDING タイトル

		# PENDING テンプレートをDOMとして読んでから中身をDOM操作で組み立てるべきか
		body = self.body(model_list)
		#form = self.form()
		html = _html().format(title=title, body=body)

		doc = minidom.parseString(html.replace("\t", "").replace("\n", ''))
		#header("Content-Type: text/html charset=UTF-8")
		return doc.toprettyxml()[23:] # XML宣言削除

	# PENDING HTMLバージョンいくつ宣言にする？

	def body(self, model_list):
		mmm = '<div>'
		for num, model in enumerate(model_list):
			if num > 0: # 2件以上あるとき改行
				mmm += '<br/>'
			mmm += str(num) + ' ' + model.id + ' ' + model.title + ' ' + model.tag + ' ' + model.body + ' ' + model.datetime
		# mmm += str(num) + ' ' + model.id + ' ' + model.title + ' ' + model.tag + ' ' + model.body
		mmm += '</div>'

		return mmm


def _html():
	html_str = """
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html charset=UTF-8" />
		<title>{title}</title>
	</head>
	<body>
		{body}
		<form method="get" action="/">
			<input type="hidden" name="Data.post" /><br/>
			id：<input type="text" name="id" /><br/>
			title：<input type="text" name="title" /><br/>
			tag：<input type="text" name="tag" /><br/>
			body：<input type="text" name="body" /><br/>
			datetime：<input type="text" name="datetime" /><br/>
			<input type="submit" value="submit" />
		</form>
	</body>
</html>
"""
	return html_str
