import unittest

from myapp.common import database
from myapp.model.basedata import BaseData


class TestBaseData(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#database.get_connection('/var/tmp/test.sqlite3db')  # PENDING 引数仮
		database.get_connection(':memory:')  # PENDING 引数仮
		BaseData.create_table()

		#テストデータインサート
		database.connection.executemany("insert into BaseData values (?, ?, ?, ?, ?)", [
			("20121231235959123456", 'dummy', 'dummy_tag1 dummy_tag2', 'dummy body', '2012-12-31 23:59:59.123456')])

	@classmethod
	def tearDownClass(cls):
		BaseData.commit()
		database.connection.close()

	def setUp(self):
		self.obj = BaseData()

	def test_dummydata(self):  # PENDING FIX ME 行がアレなのどうする
		c = database.connection.cursor()
		c.execute("select * from BaseData")
		#for row in c: # rowはtuple
		# print(row[0], row[1], row[2], row[3], row[4])
		row = c.fetchone()
		self.assertEqual(row[0], '20121231235959123456')

	def test_init(self):
		obj = BaseData()
		self.assertIsInstance(obj, BaseData)
		self.assertEqual(obj.id, '')

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

		self.obj.load_by_id('20121231235959123456')
		self.assertEqual(self.obj.id, '20121231235959123456')
		self.assertEqual(self.obj.title, 'dummy')

	def test_save(self):
		#上書き保存
		self.obj.load('20121231235959123456')
		self.obj.title = 'dummy2'
		self.assertTrue(self.obj.save())

		self.obj.load_by_id('20121231235959123456')
		self.assertEqual(self.obj.id, '20121231235959123456')
		self.assertEqual(self.obj.title, 'dummy2')

		#新規登録
		obj = BaseData()
		obj.id = '20121231235959999999'
		obj.title = 'test'
		self.assertTrue(obj.save())

		self.obj.load_by_id('20121231235959999999')
		self.assertEqual(self.obj.id, '20121231235959999999')
		self.assertEqual(self.obj.title, 'test')

	def test_save_as(self):
	#別IDとして書き込み
	#		self.obj.load('20121231235959123456')

		obj = BaseData()
		obj.id = '20121231235959999888'
		obj.title = 'test as'
		self.assertTrue(obj.save())

		self.obj.load('20121231235959999888')
		self.obj.id = '20121231235959777777'
		self.obj.title = 'test as2'
		self.assertTrue(self.obj.save_as())

		self.obj.load('20121231235959777777')
		self.assertEqual(self.obj.id, '20121231235959777777')
		self.assertEqual(self.obj.title, 'test as2')


	#p.pprint(obj.entity.__dict__)


	def test_load_list(self):
		list_ = BaseData.load_list()
		self.assertEqual(list_[0].id, '20121231235959123456')
		self.assertEqual(list_[0].title, 'dummy')


#新しいものから取得
#古いものから取得
#期間を指定して取得
#タグで取得
#タグ一覧
#タイトル一覧
#タイトル部分一致で取得


#仕様 DBとマップするだけのはentityとして別にするか＞しない



if __name__ == '__main__':
	unittest.main()
