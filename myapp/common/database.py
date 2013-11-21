"""
共通データベース
# myapp.common.database
"""
import sqlite3

#	コネクションを保持 sqlite PostgreSQL
#	複数のコネクション持つ マスタースレーブ 垂直分割
#	エンティティ毎のコネクション管理
connection = None

#@property
#def connection() -> sqlite3.Connection:
#	"""
#	test
#	@return:
#	"""
#	return _connection
#
#
#@connection.setter
#def connection(val: sqlite3.Connection):
#	"""
#	test
#	@param val:
#	@return:
#	"""
#	global _connection
#	_connection = val


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
	val_list = []
	placeholder = ''
	for k, v in entity.__dict__.items():
		if k[0] != '_':
			keys += '`' + k + '`,'
			val_list.append(v)
			placeholder += '?,'
	keys = keys[0:-1]
	placeholder = placeholder[0:-1]
	name = entity.__class__.__name__
	sql = "insert into %s (%s) values (%s)" % (name, keys, placeholder)
	connection.execute(sql, tuple(val_list))


def update(entity):
	#PENDING プライマリキー変更するときの処理考える
	set_ = ''
	vals = list()
	for k, v in entity.__dict__.items():
		if k[0] != '_':
			set_ += '`' + k + '` = ? ,'
			vals.append(v)
	vals.append(entity.__dict__[entity._key])  # PENDING 複合キーの時どうするか
	name = entity.__class__.__name__
	sql = "UPDATE %s SET %s WHERE %s = ?" % (name, set_[0:-1], entity._key)
	connection.execute(sql, tuple(vals))


def select(entity, parameter: list):
	"""

	@param entity:
	@param parameter: [(key:val),(key:val)...]
	"""
	where = ''
	val_list = []
	for item in parameter:
		if item[0][0] != '_':
			where += '`' + item[0] + '` = ? AND ,'
			val_list.append(item[1])

	name = entity.__class__.__name__
	sql = "SELECT * FROM `%s` WHERE %s LIMIT 1" % (name, where[0:-5])
	connection.row_factory = sqlite3.Row
	cursor = connection.execute(sql, tuple(val_list))
	row = cursor.fetchone()
	for k in row.keys():
		entity.__dict__[k] = row[k]

#PENDING 1件のもリストで返す？


def select_list(entity_class, parameter: list):
	where = ''
	val_list = []
	if parameter:
		for item in parameter:
			if item[0][0] != '_':
				where += '`' + item[0] + '` = ? AND ,'
				val_list.append(item[1])

	name = entity_class.__name__
	sql = "SELECT * FROM `%s`" % name
	if parameter:
		sql += " WHERE %s" % where[0:-5]

	connection.row_factory = sqlite3.Row
	cursor = connection.execute(sql, tuple(val_list))

	ret_list = []
	for row in cursor:
		entity = entity_class()
		for k in row.keys():
			entity.__dict__[k] = row[k]
		ret_list.append(entity)
	return ret_list


def execute(query):
	connection.execute(query)
