import unittest
from myapp.common import Utility


class MyTestCase(unittest.TestCase):
	def test_something(self):
		Utility.pppp()
		self.assertEqual(True, True)
		self.assertEqual(False, False)


if __name__ == '__main__':
	unittest.main()
