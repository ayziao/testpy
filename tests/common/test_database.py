"""
データベース単体テスト
"""
import unittest
import sqlite3

from myapp.common import database


class dummy():
	def __init__(self):
		self.num = 0
		self.str = ''
		self._load_data = {}
		self._key = 'num'


class TestDataBase(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		database.connection = sqlite3.connect(":memory:")  #TODO テストの時はメモリ webアプリ起動でファイル
		cls.sql = "CREATE TABLE dummy (num int(10) NOT NULL,str varchar(500) NOT NULL, PRIMARY KEY(num))"
		database.execute(cls.sql)
		d = dummy()
		d.num = 999
		d.str = 'testdata'
		database.insert(d)


	def test_get_connection(self):
		database.get_connection(None)

	#entityかデータベース情報をもとにコネクション返す

	#	DDL生成（管理用DBクラスに分ける？）
	def test_create_ddl(self):
		ret = database.create_ddl(None)
		self.assertEqual(self.sql, ret)

	def test_insert(self):
		d = dummy()
		database.insert(d)
		d.num = 1
		d.str = 'hoge'
		database.insert(d)
		#d.num = 2
		#d.str = 'piyo'
		#database.insert(d)

		c = database.connection.cursor()
		c.execute("select num,str from dummy where num = 1")
		for row in c: # rowはtuple
			self.assertEqual(row[0], d.num)
			self.assertEqual(row[1], d.str)
		#from pprint import pprint
		#pprint(row)


	def test_update(self):
		d = dummy()
		d.num = 3
		d.str = 'spam'
		database.insert(d)
		d.str = 'ham'
		database.update(d)
		c = database.connection.cursor()
		c.execute("select num,str from dummy where num = 3")
		for row in c: # rowはtuple
			self.assertEqual(row[0], d.num)
			self.assertEqual(row[1], d.str)


	def test_select(self):
		d = dummy()
		database.select(d, [('num', 999)])
		self.assertEqual(d.num, 999)
		self.assertEqual(d.str, 'testdata')


	def test_select_list(self):
		ret = database.select_list(dummy, [])
		self.assertEqual(ret[0].num, 999)
		self.assertEqual(ret[0].str, 'testdata')
		self.assertEqual(ret[1].num, 0)
		self.assertEqual(ret[1].str, '')
		self.assertEqual(ret[2].num, 1)
		self.assertEqual(ret[2].str, 'hoge')

		d = dummy()
		d.num = 998
		d.str = 'testdata'
		database.insert(d)

		ret = database.select_list(dummy, [('str', 'testdata')])
		self.assertEqual(ret[0].num, 999)
		self.assertEqual(ret[0].str, 'testdata')
		self.assertEqual(ret[1].num, 998)
		self.assertEqual(ret[1].str, 'testdata')

	#for i in ret:
	#	print(i.__dict__)

	def test_execute(self):
		sql = "CREATE TABLE dummy2 (num int(10) NOT NULL,str varchar(500) NOT NULL, PRIMARY KEY(num))"

		database.execute(sql)

		database.connection.row_factory = sqlite3.Row
		c = database.connection.cursor()

		c.execute("select * from sqlite_master where name = 'dummy2'")
		row = c.fetchone()
		#		print(row.keys())
		self.assertEqual(row['name'], 'dummy2')


# PENDING データベースアプリを何にするか sqlite Postgres キーバリューストア
# PENDING トランザクションの仕組みはどうするか
# PENDING 複数サーバ 複数DB を考慮するか

if __name__ == '__main__':
	unittest.main()
