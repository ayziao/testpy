"""
# myapp.main
"""
from datetime import datetime

now = datetime.utcnow()

import sys
import os

path = os.path.dirname(os.path.abspath(__file__)).rstrip('myapp')
sys.path.append(path)

from myapp.common import settings

settings.setting_encode()

from myapp.common import application


def main():
	return application.main()


if __name__ == '__main__':
	# PENDING コマンドラインで使うときやバッチで使うときのこと考える
	print(__name__)
	settings.start_time = now
	res = main()
	print(res.headers)
	print(res.status)
	print(res.body)
