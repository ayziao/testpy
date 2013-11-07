"""
# myapp.controller.data
"""

from myapp.common.request import Request
from myapp.common.response import Response


class Data():
	"""
	# データコントローラ
	"""

	def __init__(self, req:Request):
		self.request = req

	def run(self):
		"""
		実行
		"""
		res = Response()
		return res


	#データ/キーワードエントリ
	#データ/IDエントリ
	#データ/キーワード一覧
	#データ/ID一覧
	#データ/ディレクトリ一覧
	#データ/タグ一覧
	#データ/検索
	#データ/タグタイムライン
	#データ/タイトルタイムライン
	#データ/IDタイムライン
	#データ/IDタイムライン 年月日
	#データ/ディレクトリ内タイトルタイムライン

	#


#ユースケースは？
#●短文投稿
#タイトル無し タグ無し 短文投稿
#ベースデータへ登録
#投稿完了をflash
#タイムラインへ登録
#パッシブプラグインフック
#
#●長文投稿
#タイトルあり タグあり 長文投稿
#	タイトル欄なしモードの時は本文1行目をタイトルにする
#ベースデータへ登録
#投稿完了をflash
#タイムラインへ登録
#表示用データ更新or登録
#タイトルリスト更新or登録
#タグリスト更新or登録
#
#パッシブプラグインフック
