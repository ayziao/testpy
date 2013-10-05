from wsgiref import simple_server
from myapp.wsgi_client import application


def make_server():
	server = simple_server.make_server('', 8080, application)
	server.serve_forever()


if __name__ == '__main__':
	make_server()

