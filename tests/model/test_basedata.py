import unittest
import sqlite3

from myapp.common import database
from myapp.model.basedata import BaseData
from myapp.model.basedata import BaseDataEntity


class TestBaseData(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		database.connection = sqlite3.connect(":memory:")
		aaa = BaseDataEntity(database.connection)
		aaa.create()

		#sql = """
		#create table BaseData (
		#	id varchar(20),
		#	title varchar(500),
		#	tag varchar(500),
		#	body text,
		#	datetime text
		#);
		#"""
		#database.connection.execute(sql)
		database.connection.executemany(
			"insert into BaseData values (?, ?, ?, ?, ?)",
			[("20121231235959123456", 'dummy', 'dummy_tag1 dummy_tag2', 'dummy body', '2012-12-31 23:59:59.123456')]
		)


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

		self.obj.load_by_id('20121231235959123456')
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
