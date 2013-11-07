import unittest

from myapp.model.basedata import BaseData


class TestBaseData(unittest.TestCase):
	def test_init(self):
		obj = BaseData()
		self.assertIsInstance(obj, BaseData)

#新規作成
#読み込み
#	ID
#	タイトル
#書き込み
#別IDとして書き込み

#新しいものから取得
#古いものから取得
#期間を指定して取得
#タグで取得
#タグ一覧
#タイトル一覧
#タイトル部分一致で取得


#PENDING DBとマップするだけのはentityとして別にするか



if __name__ == '__main__':
	unittest.main()
