import sys
import os
from datetime import datetime

path = os.path.dirname(os.path.abspath(__file__)).rstrip('myapp')
sys.path.append(path)

from myapp.common import Utility
import myapp.common.initializesetting as ini
from myapp.myapp_main import main

ini.set_config_directory(path.join('config/'))


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
