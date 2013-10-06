from pprint import pprint
from datetime import datetime


class debug:
	def count(self):  # PENDING プラグイン化
		tstr = '2013-10-06 23:59:59'  # TODO 設定ファイルからとる
		from_ = datetime.strptime(tstr, '%Y-%m-%d %H:%M:%S')
		to = datetime.now()
		count = from_ - to
		return count

	def print(self):
		pprint(globals())


if __name__ == '__main__':
	c = debug()
	count = c.count()
	print(count)
	c.print()

