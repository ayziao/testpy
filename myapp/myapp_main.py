from datetime import datetime

now = datetime.utcnow()

import sys
import os

path = os.path.dirname(os.path.abspath(__file__)).rstrip('myapp')
sys.path.append(path)

from myapp.common import Utility
from myapp.common.application import Application

Utility.set_mypath(path)
Utility.set_start_time(now)


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
		Utility.debug_print(env)
		print(res.status)

