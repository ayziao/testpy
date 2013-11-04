"""
# myapp.controller.top
"""

from myapp.common import application


class Top():
	"""
	# サイトトップコントローラ
	"""

	def __init__(self):
		self.title = ''
		self.temp = 'Hello world!'

	def run(self):
		"""
		実行
		"""
		app = application.get_instance()
		app.response.body = self.title
		app.response.body = self.temp


#扉型
#ダッシュボード、タイムライン型
#メニュー型

