"""
# myapp.common.Utility
"""
#TODO ファイル名頭文字大文字なので作りなおす
#TODO それぞれクラス作って移動する

from datetime import datetime


def count():  # PENDING プラグイン化
	tstr = '2013-10-06 23:59:59'  # TODO 設定ファイルからとる
	from_ = datetime.strptime(tstr, '%Y-%m-%d %H:%M:%S')
	to = datetime.now()
	return from_ - to


if __name__ == '__main__':
	print(count())
