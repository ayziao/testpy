"""
# myapp.wsgiclient
"""
from datetime import datetime

now = datetime.utcnow()

import sys
import os

# PENDING やっぱりmainに混ぜる？

path = os.path.dirname(os.path.abspath(__file__)).rstrip('myapp')
sys.path.append(path)

from myapp.common import settings

settings.setting_encode()
settings.wsgi_load_time = now

import myapp.common.application

# PENDING セッションとかwebサーバのあれこれの処理はここでやる？


def application(environ: dict, start_response: 'function(status: str, header: list[tuple(key,value)])'):
	"""
	# WSGI application
	#
	# WSGIサーバから呼ばれるところ
	@param environ: webサーバ環境変数等
	@param start_response: レスポンス コールバック関数
	"""
	if environ['PATH_INFO'] == '/favicon.ico':
		# PENDING ファイル無いときの動作どうするか考える
		start_response('404 Not Found', [('Content-Type', 'text/html; charset=utf-8')])
		return ['Not Found'.encode()]
	else:
		settings.start_time = datetime.utcnow()
		settings.environ = environ
		response = myapp.common.application.main()
		start_response(response.status, response.headers)
		return [response.body.encode('utf-8')]
