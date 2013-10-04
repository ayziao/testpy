import unittest

from myapp.myapp_main import application


class MyTestCase(unittest.TestCase):
	def test_something(self):
		def st(aaa, bbb):
			pass

		self.assertEqual(True, True)
		self.assertEqual(False, False)

		env = {'PATH_INFO': '/favicon.ico'}
		ref = application(env, st)

		self.assertEqual(ref, ['value Hello world!'.encode("utf-8")])


if __name__ == '__main__':
	unittest.main()
