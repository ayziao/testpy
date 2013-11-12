"""
# myapp.model.basedata
"""
from datetime import datetime


class BaseData():
	"""
	基底データ
	"""

	def __init__(self, con, id_: str=None) -> None:
		self.con = con
		self._entity = None

		self.id = ''
		self.title = ''
		self.tag = ' '
		self.body = ''
		self.datetime = None

		if id_:
			self.load(id_)

	def load(self, str_: str) -> None:
		self.load_from_title(str_)
		if self._entity is None:
			self.load_from_id(str_)

	def load_from_id(self, id_: str) -> None:
		self._entity = BaseDataEntity(id_)
		for key, item in self._entity.__dict__.items():
			self.__dict__[key] = item

	def load_from_title(self, title: str) -> None:
		self._entity = BaseDataEntity(title)
		for key, item in self._entity.__dict__.items():
			self.__dict__[key] = item

	def save(self) -> bool:
		if self._entity is None:
			self._entity = BaseDataEntity(self.con)  # FIXME
		self._entity.id = self.id
		self._entity.title = self.title
		self._entity.tag = self.tag
		self._entity.body = self.body
		self._entity.datetime = datetime.utcnow()

		return self._entity.save()

	def save_as(self):
		pass


class BaseDataEntity:
	"""
	ダミー
	"""
	# PENDING 本物作る
	def __init__(self, con, _id: str=None):
		self.con = con
		self.id = '20121231235959123456'
		self.title = 'dummy'
		self.tag = 'dummy_tag1 dummy_tag2'
		self.body = 'dummy body'
		self.datetime = datetime.strptime('2012-12-31 23:59:59.123456', '%Y-%m-%d %H:%M:%S.%f')

	def create(self):
		sql = """
		create table BaseData (
			id varchar(20),
			title varchar(500),
			tag varchar(500),
			body text,
			datetime text
		);
		"""
		self.con.execute(sql)


	def save(self):
		return True