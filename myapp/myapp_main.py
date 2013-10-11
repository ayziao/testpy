from datetime import datetime

now = datetime.utcnow()

import sys
import os

path = os.path.dirname(os.path.abspath(__file__)).rstrip('myapp')
sys.path.append(path)

from myapp.common import settings
from myapp.common import application

path += '/config/'
settings.config_path = path


def main():
	#app = Application()
	return application.main()


if __name__ == '__main__':
	print(__name__)
	settings.start_time = now
	res = main()
	print(res.headers)
	print(res.status)
	print(res.body)
