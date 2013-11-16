"""
共通データベース
# myapp.common.database
"""

#	コネクションを保持 sqlite PostgreSQL
#	複数のコネクション持つ マスタースレーブ 垂直分割
#	エンティティ毎のコネクション管理
connection = None
_sqlite_connection = None


#entityかデータベース情報をもとにコネクション返す
def get_connection(hogehoge):
	pass

#	DDL生成（管理用DBクラスに分ける？）
def create_ddl(dbinfo):
	pass


def insert(entity):
	pass


def update(entity):
	pass


def save(entity):
	pass


def save_as(entity):
	pass


def select(entity):
	pass


def select_List(entity):
	pass

#PENDING 1件のもリストで返す？

def execut(query):
	pass

