"""
# myapp.wsgiclient
"""
from datetime import datetime

now = datetime.utcnow()

import sys
import os
from types import FunctionType

# PENDING やっぱりmainに混ぜる？

path = os.path.dirname(os.path.abspath(__file__)).rstrip('myapp')
sys.path.append(path)

from myapp.common import settings

settings.setting_encode()
settings.wsgi_load_time = now

import myapp.common.application

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
		# TODO 拒否リスト作る
		start_response('404 Not Found', [('Content-Type', 'text/html; charset=utf-8')])
		return ['Not Found'.encode()]
	else:
		settings.start_time = datetime.utcnow()
		settings.environ = environ
		response = myapp.common.application.main()
		start_response(response.status, response.headers)
		# TODO MIME typeを見て文字エンコードして返すかそのまま帰すかの処理を入れる
		return [response.body.encode('utf-8')]
