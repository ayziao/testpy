import unittest
import myapp.common.Utility


class MyTestCase(unittest.TestCase):
	def test_something(self):
		myapp.common.Utility.pppp()
		self.assertEqual(True, True)
		self.assertEqual(False, False)


if __name__ == '__main__':
	unittest.main()
