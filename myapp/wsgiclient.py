import sys
import os
from datetime import datetime

path = os.path.dirname(os.path.abspath(__file__)).rstrip('myapp')
sys.path.append(path)

from myapp.common import settings
from myapp.myapp_main import main

path += '/config/'
settings.config_path = path


def application(environ, start_response):
	"""
	# WSGI application
	#
	# WSGIサーバから呼ばれるところ
	"""
	settings.start_time = datetime.utcnow()
	settings.environ = environ
	response = main()
	start_response(response.status, response.headers)
	return [response.body.encode("utf-8")]
