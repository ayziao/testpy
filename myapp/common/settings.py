"""
# myapp.common.settings
#
# 設定データ置き場(グローバル変数的なものとか)
"""

from configparser import ConfigParser
from datetime import datetime

config_path = '../config/'
_ini = None  # 初期設定
environ = None  # WSGIサーバから渡される情報
start_time = datetime.utcnow()  # 処理開始日時


def get_ini(section=None):
	"""
	# 初期設定取得(セクション別取得)
	"""
	global _ini
	if _ini is None:
		_ini = ConfigParser()
		_ini.read(config_path + 'setting.ini')
	if section is None:
		return _ini
	else:
		return _ini[section]
