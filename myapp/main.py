"""
# myapp.main
"""
from datetime import datetime

now = datetime.utcnow()

import sys
import os
import io

path = os.path.dirname(os.path.abspath(__file__)).rstrip('myapp')
sys.path.append(path)

from myapp.common import settings

sys_ini = settings.get_ini('system')
if not sys_ini is None and sys_ini['text_encoding']:
	sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding=sys_ini['text_encoding'])
	sys.stdin = io.TextIOWrapper(sys.stdout.buffer, encoding=sys_ini['text_encoding'])

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
