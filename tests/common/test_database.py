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
		database.connection.execute(cls.sql)
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

	def test_save(self):
		database.save(None)

	def test_save_as(self):
		database.save_as(None)

	def test_select(self):
		d = dummy()
		database.select(d, [('num', 999)])
		self.assertEqual(d.num, 999)
		self.assertEqual(d.str, 'testdata')


	def test_select_list(self):
		database.select_list(None)

	def test_execut(query):
		database.execut(None)

# PENDING データベースアプリを何にするか sqlite Postgres キーバリューストア
# PENDING トランザクションの仕組みはどうするか
# PENDING 複数サーバ 複数DB を考慮するか

if __name__ == '__main__':
	unittest.main()
