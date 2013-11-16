"""
データベース単体テスト
"""
import unittest

from myapp.common import database


class TestDataBase(unittest.TestCase):
	def test_get_connection(self):
		database.get_connection(None)

	#entityかデータベース情報をもとにコネクション返す

	#	DDL生成（管理用DBクラスに分ける？）
	def test_create_ddl(self):
		database.create_ddl(None)

	def test_insert(self):
		database.insert(None)

	def test_update(self):
		database.update(None)

	def test_save(self):
		database.save(None)

	def test_save_as(self):
		database.save_as(None)

	def test_select(self):
		database.select(None)

	def test_select_List(self):
		database.select_list(None)

	def test_execut(query):
		database.execut(None)

# PENDING データベースアプリを何にするか sqlite Postgres キーバリューストア
# PENDING トランザクションの仕組みはどうするか
# PENDING 複数サーバ 複数DB を考慮するか

if __name__ == '__main__':
	unittest.main()
