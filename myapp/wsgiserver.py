from wsgiref import simple_server
import myapp.MyApp


def make_server():
	app = myapp.MyApp.application
	server = simple_server.make_server('', 8080, app)
	server.serve_forever()


if __name__ == '__main__':
	make_server()
