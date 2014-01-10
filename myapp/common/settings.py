"""
# 共通 設定モジュール
# myapp.common.settings
#
# 設定データ置き場(グローバル変数的なものとか)
# PENDING globalsモジュールかなんか作ってその下に入れたほうが良い？
#
# __main__なモジュールでpath解決の直後に書くこと
"""

import sys
import os
from configparser import ConfigParser
from datetime import datetime

# PENDING propertyにする？ゲッターセッター作る？
environ = None  # WSGIサーバから渡される情報
start_time = datetime.utcnow()  # 処理開始日時
wsgi_load_time = None  # WSGIクライアントモジュールの読み込み日時
arg = sys.argv  # コマンドライン引数

_config_path = None  # 設定ディレクトリパス
_ini = None  # 初期設定
_encode_set = False  # 文字エンコードセット済みか


def set_config_path(config_path: str):
	"""
	# 設定ファイルの位置変えるなら一番最初に呼ばれるpyファイルでこれ実行しておこう
	@param config_path: str
	"""
	global _config_path
	if _config_path is None:
		_config_path = config_path


def get_ini(section: str=None) -> ConfigParser:
	"""
	WARNING 設定ファイルの位置を変更する場合はこのメソッドを呼ぶ前にset_config_pathすること
	# 初期設定取得(セクション別取得)
	@param section: セクション名
	"""
	#PENDING section指定必須にしてini全体取るのはプロバティに分ける？
	#PENDING ConfigParserクラスだるいので辞書に変換しとく？
	if _ini is None:
		_read_ini()
	if section is None:
		return _ini
	else:
		try:
			return _ini[section]
		except KeyError:
			return None


def _read_ini():
	global _ini
	_ini = ConfigParser()

	if os.path.exists(_get_ini_path()):
		_ini.read(_get_ini_path())
	else:
		_ini.read(_get_ini_path() + '.sample')


def setting_encode():
	"""
	設定ファイルの位置を変更する場合はこのメソッドを呼ぶ前にset_config_pathすること
	@return:
	"""
	# PENDING プロバティにする
	# pending ConfigParserクラスだるいので辞書に変換しとく
	global _encode_set
	sys_ini = get_ini('system')
	if not sys_ini is None and sys_ini['text_encoding'] and _encode_set is False:
		# PENDING バッファどうにかする
		#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding=sys_ini['text_encoding'])
		#sys.stdin = io.TextIOWrapper(sys.stdout.buffer, encoding=sys_ini['text_encoding'])
		#sys.stdin = open(sys.stdin.fileno(), encoding=sys_ini['text_encoding'])
		#sys.stdout = open(sys.stdout.fileno(), 'w', encoding=sys_ini['text_encoding'])
		#sys.stderr = open(sys.stderr.fileno(), 'w', encoding=sys_ini['text_encoding'])
		_encode_set = True


#プライベート
def _get_ini_path() -> str:
	if _config_path is None:
		return _default_path()
	else:
		return _config_path + 'setting.ini'


def _default_path() -> str:
	path = os.path.dirname(os.path.abspath(__file__))
	return str(path.replace('myapp/common', '')) + 'config/setting.ini'
