import unittest
from myapp.common import debug


class TestDebug(unittest.TestCase):
	def test_collect(self):
		debug.init()
		debug._collect()
		l = []
		for v in debug.get_messages():
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

	# TODO テスト書く