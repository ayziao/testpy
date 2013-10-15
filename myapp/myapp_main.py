from datetime import datetime

now = datetime.utcnow()

import sys
import os

path = os.path.dirname(os.path.abspath(__file__)).rstrip('myapp')
sys.path.append(path)

from myapp.common import settings

path += 'config/'
settings.set_config_path(path)

from myapp.common import application


def main():
	return application.main()


if __name__ == '__main__':
	print(__name__)
	settings.start_time = now
	res = main()
	print(res.headers)
	print(res.status)
	print(res.body)
