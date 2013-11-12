import unittest
import sqlite3

from myapp.model.basedata import BaseData

con = None


class TestBaseData(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		global con
		con = sqlite3.connect(":memory:")
		#aaa = BaseDataEntity(con)
		#aaa.create()

		con = sqlite3.connect(":memory:")
		sql = """
		create table BaseData (
			id varchar(20),
			title varchar(500),
			tag varchar(500),
			body text,
			datetime text
		);
		"""
		con.execute(sql)


	@classmethod
	def tearDownClass(cls):
		con.close()


	def setUp(self):
		self.obj = BaseData(con)


		#sql = "insert into user values ('jon', 26, 'USA')"
		#con.execute(sql)
		con.executemany("insert into BaseData values (?, ?, ?, ?, ?)",
		                [
			                ("20121231235959123456", 'dummy', 'dummy_tag1 dummy_tag2', 'dummy body',
			                 '2012-12-31 23:59:59.123456'),
		                ])


	def test_aaaaa(self):
		c = con.cursor()
		c.execute("select * from BaseData")
		for row in c: # rowはtuple
			print(row[0], row[1], row[2])


	def test_init(self):
		obj = BaseData(con)
		self.assertIsInstance(obj, BaseData)
		self.assertIsNone(obj._entity)

		obj = BaseData(con, '20121231235959123456')
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
		obj = BaseData(con)
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
