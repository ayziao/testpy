from myapp.common.Utility import debug_print
from myapp.common.application import Application


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
	print(res.status)
	print(res.headers)
	print(res.body)
