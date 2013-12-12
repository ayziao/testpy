"""
# myapp.model.basedata
"""

from myapp.common import database


class BaseData():
	"""
	基底データ
	"""

	@staticmethod
	def create_table():
		sql = """
		create table BaseData (
			id varchar(20) PRIMARY KEY,
			title varchar(500),
			tag varchar(500),
			body text,
			datetime text
		);
		"""
		database.execute(sql) # PENDING 何処のデータベースに作るか指定出来るように

	def __init__(self, id_: str=None) -> None:
		self.id = ''
		self.title = ''
		self.tag = ''
		self.body = ''
		self.datetime = None
		self._key = 'id'

		if id_:
			self.load(id_)

	def load(self, str_: str) -> None:
		ret = self.load_by_title(str_)
		if ret == '':
			ret = self.load_by_id(str_)
		return self.id

	def load_by_id(self, id_: str) -> None:
		prm = [('id', id_)]
		database.select(self, prm)
		return self.id

	def load_by_title(self, title: str) -> None:
		prm = [('title', title)]
		database.select(self, prm)
		return self.id

	def save(self) -> bool:
		if self.id != '':
			return database.connection.executemany(
				"UPDATE  BaseData set id=?, title=?, tag=?, body=?, datetime=?",
				[(self.id, self.title, self.tag, self.body, self.datetime)]
			)

	def save_as(self):
		if self.id != '':
			return database.connection.executemany(
				"insert into BaseData values (?, ?, ?, ?, ?)",
				[(self.id, self.title, self.tag, self.body, self.datetime)]
			)

	@classmethod
	def load_list(cls):
		# database.get_connection()
		return database.select_list(BaseData, None)

	@classmethod
	def commit(cls):
		database.connection.commit()
