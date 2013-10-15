"""
# myapp.common.settings
#
# 設定データ置き場(グローバル変数的なものとか)
"""

import sys
import os
from configparser import ConfigParser
from datetime import datetime

_config_path = None
_ini = None  # 初期設定
environ = None  # WSGIサーバから渡される情報
start_time = datetime.utcnow()  # 処理開始日時
arg = sys.argv  # コマンドライン引数


def set_config_path(config_path):
	"""
	# 設定ファイルの位置変えるなら一番最初に呼ばれるpyファイルでこれ実行しておこう
	"""
	global _config_path
	if _config_path is None:
		_config_path = config_path


def get_ini(section=None):
	"""
	# 初期設定取得(セクション別取得)
	"""
	global _ini
	if _ini is None:
		_ini = ConfigParser()
		_ini.read(_get_ini_path())
	if section is None:
		return _ini
	else:
		return _ini[section]


def _get_ini_path():
	if _config_path is None:
		path = os.path.dirname(os.path.abspath(__file__))
		path = path.replace('myapp/common', '')
		path += 'config/setting.ini'
		return path
	else:
		return _config_path + 'setting.ini'

