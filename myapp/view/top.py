"""
# myapp.view.top
"""
# TODO投稿フォーム
from xml.dom import minidom

from myapp.common import settings
from myapp.common import application
from myapp.common import request


class Top:
	"""
	トップページ
	"""

	def view(self):
		if (settings.environ):
			self.viewhtml()
		else:
			print('top')

	def viewhtml(self):
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


	def form(self):
		navhtml = ''
		formhtml = ''
		isLogin = True
		if isLogin:
			#PENDING どうにか
			#include dirname(__FILE__) . '/parts/post_form.php'
			navhtml += '<a href="./?Account.logout">logout</a><br><br>'
		else:
			navhtml += '<a href="./?Account.signup">signup</a><br>'
			navhtml += '<a href="./?Account.login">login</a><br><br>'

		nav_request = request.create_instance()
		nav_request.controller_class_name = 'Navigation'
		nav_request.method_name = 'main'
		nav_request.extension = 'htmlElement'

		navhtml += application.run()

		return formhtml + navhtml
