"""
# myapp.controller.content

from myapp.controller.content import Content
"""
from myapp.common.request import Request


class Content():
	"""
	コンテンツ コントローラ
	リクエストのpathに該当するデータを取って返す
	"""

	def __init__(self, req: Request):
		self.request = req

	def run(self):
		"""
		実行(パス解析)
		@return:
		"""
		path = self.request.path
		if path.isdecimal():
			if len(path) == 20:
				return self.get_id

		return False

	def get_id(self):  # PENDING なんかいいメソッド名考える
		pass



		# IDフル指定の場合
		# ID途中までの場合(年リスト 月リスト 日リスト 時リスト 分リスト？ 秒リスト？)
		# タイトルの場合
		# タイトルツリーのツリー部分の場合

		#PENDING 閲覧制限 自分だけ(下書きとかログイン時だけ見れる) 許可したノードのみ(鍵でも渡すか) 全公開(デフォルト)