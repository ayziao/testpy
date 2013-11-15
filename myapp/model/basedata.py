"""
# myapp.model.basedata
"""

from myapp.common import database


class BaseData():
	"""
	基底データ
	"""

	@staticmethod
	def create():
		sql = """
		create table BaseData (
			id varchar(20),
			title varchar(500),
			tag varchar(500),
			body text,
			datetime text
		);
		"""
		database.connection.execute(sql)

	def __init__(self, id_: str=None) -> None:
		self.id = ''
		self.title = ''
		self.tag = ' '
		self.body = ''
		self.datetime = None

		if id_:
			self.load(id_)

	def load(self, str_: str) -> None:
		ret = self.load_by_title(str_)
		if ret == '':
			ret = self.load_by_id(str_)
		return self.id

	def load_by_id(self, id_: str) -> None:
		c = database.connection.cursor()
		c.execute("select * from BaseData where title='" + id_ + "'")
		for row in c: # rowはtuple
			self.id = row[0]
			self.title = row[1]
			self.tag = row[2]
			self.body = row[3]
			self.datetime = row[4]
		return self.id


	def load_by_title(self, title: str) -> None:
		c = database.connection.cursor()
		c.execute("select * from BaseData where title='" + title + "'")
		for row in c: # rowはtuple
			self.id = row[0]
			self.title = row[1]
			self.tag = row[2]
			self.body = row[3]
			self.datetime = row[4]
		return self.id


	def save(self) -> bool:
		if self.id != '':
			database.connection.executemany(
				"UPDATE  BaseData set id=?, title=?, tag=?, body=?, datetime=?)",
				[(self.id, self.title, self.tag, self.body, self.datetime)]
			)


	def save_as(self):
		if self.id != '':
			return database.connection.executemany(
				"insert into BaseData values (?, ?, ?, ?, ?)",
				[(self.id, self.title, self.tag, self.body, self.datetime)]
			)

