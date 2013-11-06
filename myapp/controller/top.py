"""
# myapp.controller.top
"""

from myapp.common.request import Request
from myapp.view.top import Top as ViewTop


class Top():
	"""
	# サイトトップコントローラ
	"""

	def __init__(self, req:Request):
		self.title = 'Top'
		req.title = self.title
		self.request = req

	def run(self):
		"""
		実行
		"""
		view = ViewTop(self.request)
		return view.view(None)


#扉型
#ダッシュボード、タイムライン型
#メニュー型

