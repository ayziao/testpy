"""
共通データベース
# myapp.common.database
"""
import sqlite3

from myapp.common import settings

# PENDING sqlite3 PostgreSQL どう使い分けるか クラス別にするか
# PENDING コネクションを保持 PostgreSQL
# PENDING 複数のコネクション持つ マスタースレーブ 垂直分割
# PENDING エンティティ毎のコネクション管理


connection = None  #コネクションを保持 sqlite3


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
def get_connection(con=None):
	#PENDING テストの時はメモリ webアプリ起動でファイル 設定ファイルで対応
	global connection
	if con:
		connection = sqlite3.connect(con)
		return

	ini = settings.get_ini('database')
	db_file = ini.get('sqlite')
	if db_file:
		connection = sqlite3.connect(db_file)
	else:
		connection = sqlite3.connect(":memory:")


#	DDL生成（管理用DBクラスに分ける？）
def create_ddl(dbinfo):
	c = connection.cursor()
	c.execute('select * from sqlite_master')
	for row in c:
		return row[4]  # PENDING テーブル指定


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
	sql = "insert into {table_name} ({key}) values ({val})"
	sql = sql.format(table_name=name, key=keys, val=placeholder)
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
	sql = "UPDATE {table_name} SET {set} WHERE {where} = ?"
	sql = sql.format(table_name=name, set=set_[0:-1], where=entity._key)
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
			where += '`' + item[0] + '` = ? AND '
			val_list.append(item[1])

	name = entity.__class__.__name__
	sql = "SELECT * FROM `{table_name}` WHERE {where} LIMIT 1"
	sql = sql.format(table_name=name, where=where[0:-4])
	connection.row_factory = sqlite3.Row
	cursor = connection.execute(sql, tuple(val_list))
	row = cursor.fetchone()

	try: #PENDING ０件の時の処理はこれでいいか？
		for k in row.keys():
			entity.__dict__[k] = row[k]
	except AttributeError:
		pass


def select_list(entity_class, parameter: list, order: list=None):
	where = ''
	val_list = []
	if parameter:
		for item in parameter:
			if item[0][0] != '_':
				# PENDING フィールド名を英数チェックするか
				where += '`' + item[0] + '` = ? AND ,'
				val_list.append(item[1])

	if order:
		a_str = map(str, order)
		# PENDING フィールド名を`で囲うか？
		order_str = ",".join(a_str)

	name = entity_class.__name__
	sql = "SELECT * FROM `{}`".format(name)
	if parameter:
		sql += " WHERE {}".format(where[0:-5])
	if order:
		sql += " ORDER BY {}".format(order_str)

	# PENDING connection が無いときのエラー処理
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
	return connection.execute(query)
