"""
# myapp.main
"""
from datetime import datetime

now = datetime.utcnow()

import sys
import os
import pprint as p

path = os.path.dirname(os.path.abspath(__file__)).rstrip('myapp')
sys.path.append(path)

from myapp.common import settings

settings.setting_encode()

import myapp.common.application


def main() -> str:
	"""
	# コマンドライン向け
	@return:
	"""
	# PENDING 引数や設定みてヘッダ出さないとか入れる
	settings.start_time = now
	out = ''
	res = myapp.common.application.main()
	for v in res.headers:
		out += p.pformat(v) + "\n"
	out += res.status + "\n"
	out += res.body
	return out


if __name__ == '__main__':
	print(main())  # pragma: no cover
