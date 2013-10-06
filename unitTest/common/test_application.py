import unittest

from myapp.common.application import Application


class TestApplication(unittest.TestCase):
	def something(self):
		self.assertEqual(True, False)

	def test_main(self):
		app = Application()
		ret = app.main()
		self.assertEqual(ret.body, 'Hello world!')


if __name__ == '__main__':
	unittest.main()
