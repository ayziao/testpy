import sys
import os
from datetime import datetime

path = os.path.dirname(os.path.abspath(__file__)).rstrip('myapp')
sys.path.append(path)

from myapp.common.Utility import set_mypath
from myapp.common.Utility import set_environ
from myapp.common.Utility import set_start_time
from myapp.myapp_main import main

set_mypath(path)


def application(environ, start_response):
	"""
	# WSGI application
	#
	# WSGIサーバから呼ばれるところ
	"""
	set_start_time(datetime.utcnow())
	set_environ(environ)
	response = main()
	start_response(response.status, response.headers)
	return [response.body.encode("utf-8")]
