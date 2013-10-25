"""
# myapp.wsgiclient
"""

import sys
import os
from datetime import datetime

# PENDING やっぱりmainに混ぜる？

path = os.path.dirname(os.path.abspath(__file__)).rstrip('myapp')
sys.path.append(path)

from myapp.common import settings

settings.setting_encode()

import myapp.common.application as myapp


# PENDING セッションとかwebサーバのあれこれの処理はここでやる？

def application(environ: dict, start_response: 'function(status: str, header: tuple)'):
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
		return ['Not Found'.encode("utf-8")]
	else:
		settings.start_time = datetime.utcnow()
		settings.environ = environ
		response = myapp.main()
		start_response(response.status, response.headers)
		return [response.body.encode("utf-8")]
