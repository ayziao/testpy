import unittest
from myapp.common.debug import Debug


class TestDebug(unittest.TestCase):
	def test_print(self):
		d = Debug()
		d.print()


if __name__ == '__main__':
	unittest.main()