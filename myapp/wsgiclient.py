import sys
import os
from datetime import datetime

path = os.path.dirname(os.path.abspath(__file__)).rstrip('myapp')
sys.path.append(path)

from myapp.common import Utility
from myapp.myapp_main import main


Utility.set_mypath(path)


def application(environ, start_response):
	"""
	# WSGI application
	#
	# WSGIサーバから呼ばれるところ
	"""
	Utility.set_start_time(datetime.utcnow())
	Utility.set_environ(environ)
	response = main()
	start_response(response.status, response.headers)
	return [response.body.encode("utf-8")]
