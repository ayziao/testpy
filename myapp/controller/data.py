"""
# myapp.controller.data
"""

from datetime import datetime

from myapp.common.request import Request
from myapp.common.response import Response
from myapp.model.basedata import BaseData

from myapp.view.timeline import TimeLine


class Data():
	"""
	# データコントローラ
	"""

	def __init__(self, req: Request):
		self.request = req

	def run(self):
		"""
		実行
		"""
		# TODO pathからデータ取る
		res = Response()
		return res

	def post(self):
		data = BaseData()
		prm = self.request.parameter

		time = datetime.utcnow()

		data.id = time.strftime('%Y%m%d%H%M%S%f') #TODO セッティングのスタートタイムからID作ってどっかにとっといてそれつかう
		data.title = prm['title'][0]
		data.tag = prm['tag'][0]
		data.body = prm['body'][0]
		data.datetime = time.strftime('%Y-%m-%d %H:%M:%S.%f') #TODO セッティングのスタートタイムとっといてそれつかう
		data.save_as()
		BaseData.commit()

		res = Response()
		res.body = 'post'
		return res

	def time_line(self):
		"""
		タイムライン
		"""

		array = BaseData.load_list()  # ベースデータ取得

		view = TimeLine(self.request)

		return view.view(array)

	# tmphour = -1
	# tmpdate = 0

	# res = Response()

	# from pprint import pformat
	#
	# res.body = pformat(array)
	# return res

	# 表示



	# PENDING 日や時をまたいだ処理 View側でやる？
	#for value in array:
	#	value.datetime = value.time

	#if ($tmpdate != date("Ymd", $value->datetime)) {
	#	$value->date = date("Ymd", $value->datetime);
	#	$tmpdate = $value->date;
	#	$tmphour = -1;
	#}
	#if ($tmphour != date("H", $value->datetime)) {
	#	if ($tmphour != -1) {
	#		$value->hour = date("H", $value->datetime);
	#	}
	#	$tmphour = date("H", $value->datetime);
	#}
	#$value->time = date("H:i:s", $value->datetime);
	#$value->ago = (int)((time() - $value->datetime) / 60);

	#$viw = \ViewGenerator::generateViewInstance('data_list');
	#$viw->view($array);


	#view = TimeLine(self.request)
	#return view.view(None)

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
