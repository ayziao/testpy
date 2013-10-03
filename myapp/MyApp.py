import myapp.common.Utility


def application(environ, start_response):
	myapp.common.Utility.debug_print(environ)
	response = main()
	start_response(response.status, response.headers)
	return [response.body.encode("utf-8")]


def main():
	response = myapp.common.Utility.Response()
	conf = myapp.common.Utility.load_conf()
	output_str = conf['section']['key']
	output_str += ' Hello world!'
	response.body = output_str
	return response


if __name__ == '__main__':
	print(main())

