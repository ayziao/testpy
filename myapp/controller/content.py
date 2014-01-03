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
		if path.isdecimal(): # 数値 ID指定  # TODO 半角数値だけ対象にする（ユニコード数字引っかかる）
			if len(path) == 20: # フルID
				return self.get_id()
			else:
				#TODO ID途中までの場合(年リスト 月リスト 日リスト 時リスト 分リスト？ 秒リスト？)
				pass

		#PENDING データ見るまでわからん どうする タイトルツリーのツリー部分の場合

		if len(path) > 0: # 数値以外
			return self.get_title()

		return self.get_top() # パス指定がなければトップ


	def get_id(self):  # PENDING なんかいいメソッド名考える
		# IDフル指定の場合
		pass

	def get_title(self):
		# タイトルの場合
		pass

	def get_top(self):
		# トップ
		pass

		#PENDING 閲覧制限 自分だけ(下書きとかログイン時だけ見れる) 許可したノードのみ(鍵でも渡すか) 全公開(デフォルト)