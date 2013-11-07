"""
# myapp.model.basedata
"""


class BaseData():
	"""
	ベースデータ
	"""

	def __init__(self, _id=None):
		if _id:
			self.entity = BaseDataEntity()
		else:
			self.entity = None


class BaseDataEntity:
	"""
	ダミー
	"""

	def __init__(self):
		from datetime import datetime

		self.id = '20121231235959123456'
		self.title = 'dummy'
		self.tag = 'dummy_tag1 dummy_tag2'
		self.body = 'dummy body'
		self.datetime = datetime.strptime('2012-12-31 23:59:59.123456', '%Y-%m-%d %H:%M:%S.%f')
