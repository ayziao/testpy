import unittest

from myapp.model.basedata import BaseData


class TestBaseData(unittest.TestCase):
	def test_init(self):
		obj = BaseData()
		self.assertIsInstance(obj, BaseData)


if __name__ == '__main__':
	unittest.main()
