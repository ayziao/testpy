import sys
import os
from datetime import datetime

path = os.path.dirname(os.path.abspath(__file__)).rstrip('myapp')
sys.path.append(path)

from myapp.common import Utility
from myapp.common import initializesetting
from myapp.myapp_main import main

path += '/config/'
initializesetting.set_config_directory(path)


def application(environ, start_response):
	"""
	# WSGI application
	#
	# WSGIサーバから呼ばれるところ
	"""
	Utility.set_start_time(datetime.utcnow())
	print(environ)
	response = main()
	start_response(response.status, response.headers)
	return [response.body.encode("utf-8")]
