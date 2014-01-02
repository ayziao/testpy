"""
# myapp.controller.content

from myapp.controller.content import Content
"""


class Content():
	"""
	コンテンツ コントローラ
	リクエストのpathに該当するデータを取って返す
	"""

	def run(self):
		pass

		# パス解析
		# IDフル指定の場合
		# ID途中までの場合
		# タイトルの場合
		# タイトルツリーのツリー部分の場合

		#PENDING 閲覧制限 自分だけ(下書きとかログイン時だけ見れる) 許可したノードのみ(鍵でも渡すか) 全公開(デフォルト)