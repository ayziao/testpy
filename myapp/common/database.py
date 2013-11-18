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
	c = connection.cursor()
	c.execute('select * from sqlite_master')
	for row in c:
		return row[4]  # TODO テーブル指定


def insert(entity):
	keys = ''
	vals = list()
	qqq = ''
	for k, v in entity.__dict__.items():
		if k[0] != '_':
			keys += '`' + k + '`,'
			vals.append(v)
			qqq += '?,'
	keys = keys[0:-1]
	qqq = qqq[0:-1]
	name = entity.__class__.__name__
	sql = "insert into %s (%s) values (%s)" % (name, keys, qqq)
	connection.executemany(sql, [tuple(vals)])


def update(entity):
	pass


def save(entity):
	pass


def save_as(entity):
	pass


def select(entity):
	pass


def select_list(entity):
	pass

#PENDING 1件のもリストで返す？

def execut(query):
	pass

