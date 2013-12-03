import unittest

from myapp.common import database
from myapp.model.basedata import BaseData


class TestBaseData(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		database.get_connection(None)  # PENDING 引数仮
		BaseData.create_table()

		#テストデータインサート
		database.connection.executemany("insert into BaseData values (?, ?, ?, ?, ?)", [
			("20121231235959123456", 'dummy', 'dummy_tag1 dummy_tag2', 'dummy body', '2012-12-31 23:59:59.123456')])


	@classmethod
	def tearDownClass(cls):
		database.connection.close()


	def setUp(self):
		self.obj = BaseData()


	def test_dummydata(self):  # FIXME
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

		#新規登録
		obj = BaseData()
		obj.id = '20121231235959999999'
		obj.save()

	#TODO 保存後取得して内容アサート

	def test_save_as(self):
	#別IDとして書き込み
	#		self.obj.load('20121231235959123456')
		self.obj.id = '20121231235959123457'
		self.assertTrue(self.obj.save_as())

	#TODO 保存後取得して内容アサート


	#p.pprint(obj.entity.__dict__)


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
