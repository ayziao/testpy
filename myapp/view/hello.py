"""
テスト用
"""

from myapp.common import request
from myapp.common import application


class Hello():
	"""
	はろー
	"""

	def __init__(self):
		self._aaaa = 'Hello world!'

	def view(self):
		"""
		表示
		@return:
		"""
		return self._aaaa


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
