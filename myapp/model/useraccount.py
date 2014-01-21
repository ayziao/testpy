"""
# myapp.model.useraccount
"""

from myapp.common import database

#UUID
#パスワード
#メールアドレス
#秘密鍵
#更新日時
#作成日時

#identifier
#mail address
#password hash
#password salt
#signup date
#lastLogin date

class UserAccount():
	"""
	ユーザーアカウント
	"""

	@staticmethod
	def create_table():
		sql = """
		create table UserAccount (
			identifier varchar(20) PRIMARY KEY,
			mail varchar(500),
			password varchar(500),
			signup text,
			last_login text
		);
		"""
		database.execute(sql)  # PENDING 何処のデータベースに作るか指定出来るように

	def __init__(self, identifier: str=None) -> None:
		self.identifier = ''
		self.mail = ''
		self.password = ''
		self.signup = None
		self.last_login = None
		self._key = 'identifier'
		if identifier:
			self.load_by_identifier(identifier)

	def load_by_identifier(self, identifier: str) -> None:
		prm = [('identifier', identifier)]
		database.select(self, prm)
		return self.identifier

	@classmethod
	def commit(cls):
		database.connection.commit()