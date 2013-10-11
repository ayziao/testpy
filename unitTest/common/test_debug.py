import unittest
from myapp.common.debug import Debug


class TestDebug(unittest.TestCase):
	def test_collect(self):
		d = Debug()
		d.collect()
		l = []
		for v in d.list:
			if 'memory' in v:
				l.append('memory')
			if 'start_time' in v:
				l.append('start_time')
			if 'end_time' in v:
				l.append('end_time')
			if 'dif' in v:
				l.append('dif')

		self.assertIn('memory', l)
		self.assertIn('start_time', l)
		self.assertIn('end_time', l)
		self.assertIn('dif', l)


if __name__ == '__main__':
	unittest.main()

	#TODO ;debug = std  #標準出力