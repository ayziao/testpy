import unittest

from myapp.common.application import Application


class TestApplication(unittest.TestCase):
	def test_init(self):
		app = Application()
		self.assertEqual(app.debug, None)

	def test_main(self):
		app = Application()
		ret = app.main()
		self.assertEqual(ret.body, 'Hello world!')

#TODO __init__のテスト

if __name__ == '__main__':
	unittest.main()
