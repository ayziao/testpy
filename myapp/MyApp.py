import myapp.common.Utility


def application(environ, start_response):
	myapp.common.Utility.debug_print(environ)

	response = myapp.common.Utility.Response()
	response.body = main()

	start_response(response.status, response.headers)
	return [response.body.encode("utf-8")]


def main():
	conf = myapp.common.Utility.load_conf()
	output_str = conf['section']['key']
	output_str += ' Hello world!'
	return output_str


if __name__ == '__main__':
	print(main())

