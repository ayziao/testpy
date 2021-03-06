"""
# myapp.main
"""
from datetime import datetime

now = datetime.utcnow()

import sys
import os
from pprint import pformat

#Pythonスクリプトパス解決
path = os.path.dirname(os.path.abspath(__file__)).rstrip('myapp')
sys.path.append(path)

from myapp.common import settings
from myapp.common import application as myapp


def main() -> str:
	"""
	# コマンドライン向け 共通アプリケーション呼んでheaderをどうにかしてボディ返す
	@return:
	"""
	#
	settings.setting_encode()
	settings.start_time = now
	out = ''
	res = myapp.main_run()
	for v in res.headers:
		out += pformat(v) + "\n"
	out += res.status + "\n"
	out += res.body
	return out


if __name__ == '__main__':
	print(main())  # pragma: no cover
