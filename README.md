testpy [![Build Status](https://travis-ci.org/ayziao/testpy.png?branch=master)](https://travis-ci.org/ayziao/testpy)
======
■アプリの目的は？ めっちゃ個人向けデータ蓄積システム
---------------
個人向けだけどwebサービスとして複数ユーザ扱えるようにする
ユーザは複数サイトを持てる
ユーザはエントリをたくさん投稿できる
外部データを取り込んでいろいろする


■インストール
---------------
まだ書いてない


■開発
---------------
###●UI構造
    トップ
    ドキュメント
    	エントリ
    		ID
    		タイトル
    		(編集)
    	サマリー
    		年
    		月
    		日
    		時
    		タイトルディレクトリ
    		タグ
    	(新規登録)
    公開機能
    	リスト
    		タグリスト
    		タイトルリスト
    	タイムライン
    		最新
    		特定期間
    ログイン機能
    	ダッシュボード アクティビティ
    	設定


###●ソースコード構造
ドキュメントルート webサーバの公開領域におく
設定 設置時に書く DB接続情報とか
    アプリケーション 設置時にいじらない 1ファイルアーカイブ化できるならしたい
    └共通
    └コントローラ
    └モデル
    └ビュー
    プラグイン プラグイン入れるとこ
    └プラグイン名 プラグイン作者ドメイン/プラグイン名/[共通,m,v,c,t]？
    	└コントローラ コントローラはモデルとビューを知っている actionを受け取ってモデルをコントロールして結果をviewに渡す
    	└モデル ORマップは他に持つ？モデルはコントローラもビューも知らない webだろうがCUIだろうがネイティブアプリに移植したとしても変わらない設計をする
    	└ビュー テンプレート組み込んで返したり JSON組み立てたり ビューはモデルを知っている コントローラは知らない モデルを受け取って出し分け
    ライブラリ OS組み込みじゃないのとか
    単体テスト 本番には設置不要？
    ドキュメント 本番設置不要


テンプレートはDBに持つ またはDOM操作 CSSは通常のデータ
プラグインの前処理ってなんか必要？

###●DB構造
    システムデータベース
    	キーバリュー
    	アカウント
    		ユーザ名
    		メールアドレス
    		パスワード
    ユーザデータベース
    	キーバリュー
    	データ
    		ベースデータ
    			ID
    			タイトル
    			本文
    			タグ
    			システムタグ？
    		表示
    			ID
    			タイトル
    			加工済み本文
    		管理用データ
    			ID
    			タイトル
    			本文
    		タグ_データ
    			タグ
    			データID
    		タイトル_データ
    			タイトル
    			データID
    		全文検索用
    		外部データリレーション？
    外部データ
    	ID
    	URL
    	タイトル
    	本文

    システムプラグイン
    	有効なプラグインリスト

    ユーザープラグイン（大体はキーバリューテーブルにjsonで入れる）
    	外部サイト投稿設定

###●DB使い方
マスタDBはなるべく読み込みのみ
ログDBはなるべく書き込みのみ DBじゃなくても良いように作る トランザクションなしの書きっぱなし
トランザクションDBはなるべくトランザクション使う INNODB前提でいいか

管理ツールからはそうでもない




###●予約ユーザー名
administrator admin root ユーザーログインからはログイン不可


## TODO
カバレッジ
https://coveralls.io/docs/python