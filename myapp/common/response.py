"""
# myapp.common.response
"""

_instance = []

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
		return self.__status_code

	@status_code.setter
	def status_code(self, val: int) -> None:
		self.status = str(val) + _status_messages.get(val)
		self.__status_code = val


def get_instance() -> Response:
	"""
	# 最新のスタックを返す 空なら作ってセット
	"""
	if not _instance:
		_instance.append(Response())

	return _instance[-1]


def create_instance() -> Response:
	"""
	# 新しくスタック積んで返す
	"""
	_instance.append(Response())

	return _instance[-1]


def pop_instance() -> Response:
	"""
	# 最新のスタックを取り出して返す
	"""
	if _instance:
		return _instance.pop()
	else:
		return None



