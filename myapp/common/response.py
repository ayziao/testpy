"""
# 共通 レスポンスモジュール
# myapp.common.response
"""

_status_messages = {
	200: ' OK',
	302: ' Found',
	303: ' See Other',
	304: ' Not Modified',
	307: ' Temporary Redirect',
	400: ' Bad Request',
	403: ' Forbidden',
	404: ' Not Found',
	500: ' Internal Server Error',
}


class Response():
	"""
	# レスポンス
	"""

	def __init__(self) -> None:
		"""
		# 初期化
		"""
		self.__status_code = 0
		self.status = '200 OK'
		#self.headers = [('Content-Type', 'text/plain; charset=utf-8')]
		self.headers = [('Content-Type', 'text/html; charset=utf-8')]
		self.body = ''

	@property
	def status_code(self) -> int:
		"""
		ステータスコード
		"""
		return self.__status_code

	@status_code.setter
	def status_code(self, val: int) -> None:
		"""
		ステータスコードを受け取ったらステータス文字列を組み立てる
		@param val: ステータスコード値
		"""
		self.status = str(val) + _status_messages.get(val)
		self.__status_code = val
