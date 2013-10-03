import configparser


def load_conf():
	conf = configparser.ConfigParser()
	conf.read('../config/setting.ini.sample')
	return conf


def debug_print(environ):
	if environ['PATH_INFO'] != '/favicon.ico':
		from pprint import pprint
		pprint(environ)


def application(environ, start_response):
	debug_print(environ)

	response = Response()
	response.body = main()

	start_response(response.status, response.headers)
	return [response.body.encode("utf-8")]


class Response():
	status = '200 OK'
	headers = [('Content-Type', 'text/plain; charset=utf-8')]
	body = ''


def main():
	conf = load_conf()
	output_str = conf['section']['key']
	output_str += ' Hello world!'
	return output_str


if __name__ == '__main__':
	print(main())

