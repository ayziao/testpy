import unittest
from myapp.common import utility
from myapp.common import debug


class TestUtility(unittest.TestCase):
	def test_import(self):
		mod = utility.import_('myapp.common.debug')
		self.assertEqual(mod, debug)

	def test_view_dispatcher(self):
		mod = utility.view_dispatcher('Hello')
		ret = mod.view()
		self.assertEqual(ret, 'Hello world!')


if __name__ == '__main__':
	unittest.main()
