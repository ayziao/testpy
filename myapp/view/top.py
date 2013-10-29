"""
# myapp.view.top
"""
# TODO投稿フォーム

class top:
	"""
	トップページ
	"""

	def view(self):
		bs = BaseSystem.getInstance()
		if (bs.isWebExec()):
			self.viewhtml()
		else:
			print('top')

		return True

	def viewhtml(self):
		app = Application.getInstance()
		title = app.name
		form = self.form()
		html = """
		<html>
			<head>
				<meta http-equiv="Content-Type" content="text/html charset=UTF-8">
				<title>{title}</title>
			</head>
			<body><h1>{title}</h1>{form}</body>
		</html>
"""

		doc = DOMDocument()
		doc.loadHTML(html)
		header("Content-Type: text/html charset=UTF-8")
		print(doc.saveHTML())

		app.backtrace()


	def form(self):
		navhtml = ''
		formhtml = ''
		if (Application.getInstance().isLogin()):
			#PENDING どうにか
			#include dirname(__FILE__) . '/parts/post_form.php'
			navhtml += '<a href="./?Account.logout">logout</a><br><br>'
		else:
			navhtml += '<a href="./?Account.signup">signup</a><br>'
			navhtml += '<a href="./?Account.login">login</a><br><br>'

		navquery = Query()
		navquery.controllerClassName = 'Navigation'
		navquery.methodName = 'main'
		navquery.extension = 'htmlElement'

		navhtml += Application.getInstance.stackRun(navquery)

		return formhtml + navhtml
