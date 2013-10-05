from datetime import datetime

now = datetime.utcnow()

import sys
import os

path = os.path.dirname(os.path.abspath(__file__)).rstrip('myapp')
sys.path.append(path)

from myapp.common.Utility import set_mypath
from myapp.common.Utility import set_start_time
from myapp.common.Utility import debug_print
from myapp.common.application import Application

set_mypath(path)
set_start_time(now)


def main():
	app = Application()

	return app.main()


if __name__ == '__main__':
	res = main()

	argument_list = sys.argv
	if '-debugprint' in argument_list:
		print(argument_list)
		print(res.headers)

	print(res.body)

	if '-debugprint' in argument_list:
		env = {'PATH_INFO': '/favicon.ico', 'debug': True}  # TODO デバッグ表示オフ機能つける
		debug_print(env)
		print(res.status)

