import sys
import os
from wsgiref import simple_server

path = os.path.dirname(os.path.abspath(__file__)).rstrip('myapp')
sys.path.append(path)

from myapp.wsgiclient import application


def make_server():
	server = simple_server.make_server('', 8080, application)
	server.serve_forever()


if __name__ == '__main__':
	make_server()

