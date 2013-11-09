import unittest

from myapp.model.basedata import BaseData


class TestBaseData(unittest.TestCase):
	def setUp(self):
		self.obj = BaseData()

	def test_init(self):
		obj = BaseData()
		self.assertIsInstance(obj, BaseData)
		self.assertIsNone(obj._entity)

		obj = BaseData('20121231235959123456')
		self.assertEqual(obj.id, '20121231235959123456')
		self.assertEqual(obj.title, 'dummy')

	def test_load(self):
		self.obj.load('20121231235959123456')
		self.assertEqual(self.obj.id, '20121231235959123456')
		self.assertEqual(self.obj.title, 'dummy')

		self.obj.load('dummy')
		self.assertEqual(self.obj.id, '20121231235959123456')
		self.assertEqual(self.obj.title, 'dummy')

		self.obj.load_from_id('20121231235959123456')
		self.assertEqual(self.obj.id, '20121231235959123456')
		self.assertEqual(self.obj.title, 'dummy')


	def test_save(self):
		self.obj.load('20121231235959123456')
		self.obj.title = 'dummy2'
		self.assertTrue(self.obj.save())

		#新規登録
		obj = BaseData()
		obj.id = '20121231235959999999'
		obj.save()

	@unittest.skip("demonstrating skipping")
	def test_save_as(self):
		#別IDとして書き込み
		pass


	#p.pprint(obj.entity.__dict__)


#新しいものから取得
#古いものから取得
#期間を指定して取得
#タグで取得
#タグ一覧
#タイトル一覧
#タイトル部分一致で取得


#PENDING DBとマップするだけのはentityとして別にするか



if __name__ == '__main__':
	unittest.main()
