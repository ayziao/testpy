"""
共通データベース
# myapp.common.database
"""
import sqlite3

#	コネクションを保持 sqlite PostgreSQL
#	複数のコネクション持つ マスタースレーブ 垂直分割
#	エンティティ毎のコネクション管理
_connection = None
_sqlite_connection = None

__status_code = None


@property
def connection() -> sqlite3.Connection:
	"""
	test
	@return:
	"""
	return _connection


@connection.setter
def connection(val: sqlite3.Connection):
	"""
	test
	@param val:
	@return:
	"""
	global _connection
	_connection = val


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
	connection.execute(sql, tuple(vals))


def update(entity):
	#PENDING プライマリキー変更するときの処理考える
	set = ''
	vals = list()
	for k, v in entity.__dict__.items():
		if k[0] != '_':
			set += '`' + k + '` = ? ,'
			vals.append(v)
	vals.append(entity.__dict__[entity._key])  # PENDING 複合キーの時どうするか
	name = entity.__class__.__name__
	sql = "UPDATE %s SET %s WHERE %s = ?" % (name, set[0:-1], entity._key)
	connection.execute(sql, tuple(vals))


def select(entity, parameter: list):
	"""

	@param entity:
	@param parameter: [(key:val),(key:val)...]
	"""
	where = ''
	vals = list()
	for item in parameter:
		if item[0][0] != '_':
			where += '`' + item[0] + '` = ? AND ,'
			vals.append(item[1])

	name = entity.__class__.__name__
	sql = "SELECT * FROM `%s` WHERE %s LIMIT 1" % (name, where[0:-5])
	connection.row_factory = sqlite3.Row
	c = connection.cursor()
	c.execute(sql, tuple(vals))
	row = c.fetchone()
	for k in row.keys():
		entity.__dict__[k] = row[k]


def select_list(entity):
	pass

#PENDING 1件のもリストで返す？

def execut(query):
	pass

