import unittest
from myapp.common.debug import Debug


class TestDebug(unittest.TestCase):
	def test_aaa(self):
		d = Debug()
		d.print()


if __name__ == '__main__':
	unittest.main()