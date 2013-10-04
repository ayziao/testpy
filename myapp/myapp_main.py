import sys
import os

path = os.path.dirname(os.path.abspath(__file__)).rstrip('myapp')
sys.path.append(path)

from myapp.common.Utility import setmypath
from myapp.common.Utility import debug_print
from myapp.common.application import Application

setmypath(path)


def application(environ, start_response):
	debug_print(environ)
	response = main()
	start_response(response.status, response.headers)
	return [response.body.encode("utf-8")]


def main():
	app = Application()
	return app.main()


if __name__ == '__main__':
	res = main()
	argvs = sys.argv
	if 'iroiro' in argvs:
		print(argvs)
		print(res.status)
		print(res.headers)

	print(res.body)
