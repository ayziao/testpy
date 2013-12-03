"""
# myapp.controller.error
"""
from myapp.common.response import Response


class Error():
	"""
	エラーコントローラ
	"""

	def run(self):
		res = Response()
		res.status_code = 404
