"""
# myapp.common.settings
#
# 設定データ置き場(グローバル変数的なものとか)
"""

import sys
import os
import io
from configparser import ConfigParser
from datetime import datetime

_config_path = None
_ini = None  # 初期設定
environ = None  # WSGIサーバから渡される情報
start_time = datetime.utcnow()  # 処理開始日時
arg = sys.argv  # コマンドライン引数


def set_config_path(config_path: str):
	"""
	# 設定ファイルの位置変えるなら一番最初に呼ばれるpyファイルでこれ実行しておこう
	"""
	global _config_path
	if _config_path is None:
		_config_path = config_path


def get_ini(section: str=None) -> ConfigParser:
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
		try:
			return _ini[section]
		except KeyError:
			return None


def setting_encode():
	"""
	@return:
	"""
	sys_ini = get_ini('system')
	if not sys_ini is None and sys_ini['text_encoding']:
		sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding=sys_ini['text_encoding'])
		sys.stdin = io.TextIOWrapper(sys.stdout.buffer, encoding=sys_ini['text_encoding'])


#プライベート
def _get_ini_path() -> str:
	if _config_path is None:
		path = os.path.dirname(os.path.abspath(__file__))
		return str(path.replace('myapp/common', '')) + 'config/setting.ini'
	else:
		return _config_path + 'setting.ini'





