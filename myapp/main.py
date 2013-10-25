"""
# myapp.main
"""
from datetime import datetime
import pprint as p

now = datetime.utcnow()

import sys
import os

path = os.path.dirname(os.path.abspath(__file__)).rstrip('myapp')
sys.path.append(path)

from myapp.common import settings

settings.setting_encode()

import myapp.common.application as myapp


def main() -> str:
	"""
	# コマンドライン向け
	@return:
	"""
	settings.start_time = now
	out = ''
	res = myapp.main()
	for v in res.headers:
		out += p.pformat(v) + "\n"
	out += res.status + "\n"
	out += res.body
	return out


if __name__ == '__main__':
	print(main())