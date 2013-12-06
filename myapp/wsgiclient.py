"""
# myapp.wsgiclient
"""
from datetime import datetime

now = datetime.utcnow()

import sys
import os
from types import FunctionType

path = os.path.dirname(os.path.abspath(__file__)).rstrip('myapp')
sys.path.append(path)

from myapp.common import settings

settings.setting_encode()
settings.wsgi_load_time = now

from myapp.common import application as myapp

# PENDING セッションとかwebサーバのあれこれの処理はここでやる？


def application(environ: dict, start_response: FunctionType):
	"""
	# WSGI application
	#
	# WSGIサーバから呼ばれるところ
	@param environ: webサーバ環境変数等
	@param start_response: レスポンス コールバック関数  function(status: str, header: [(key: str,value: str), ...])
	"""
	if environ['PATH_INFO'] == '/favicon.ico':
		# PENDING 拒否リスト作る
		# PENDING ファビコンどうするか
		start_response('404 Not Found', [('Content-Type', 'text/html; charset=utf-8')])
		return ['Not Found'.encode()]
	else:
		settings.start_time = datetime.utcnow()
		settings.environ = environ
		response = myapp.main_run()
		start_response(response.status, response.headers)
		# PENDING MIME typeを見て文字エンコードして返すかそのまま帰すかの処理を入れる Viewに入れるべきか utility化するか
		return [response.body.encode('utf-8')]
