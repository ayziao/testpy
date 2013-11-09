"""
テスト用
"""

from myapp.common.request import Request
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
		"""
		入力フォームとか
		@return:
		"""
		navi_html = ''
		form_html = ''
		is_login = True
		if is_login:
			#PENDING どうにか
			#include dirname(__FILE__) . '/parts/post_form.php'
			navi_html += '<a href="./?Account.logout">logout</a><br><br>'
		else:
			navi_html += '<a href="./?Account.signup">signup</a><br>'
			navi_html += '<a href="./?Account.login">login</a><br><br>'

		nav_request = Request()
		nav_request.controller_class_name = 'Navigation'
		nav_request.method_name = 'main'
		nav_request.extension = 'htmlElement'

		navi_html += application.run(nav_request)

		return form_html + navi_html
