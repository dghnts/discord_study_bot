# Discord作業時間計測BOT(仮)

## 概要

- bot起動時にBotが作業用サーバーにログイン
- ユーザーが作業用VCにログインすることで作業時間の計測を開始
- ユーザーがVC退室時に作業時間を記録＆作業時間をチャットに投稿
- `!status`コマンドでユーザーの累積学区集時間を表示
- `!daily`コマンドでユーザーの今日の作業時間を表示

## ディレクトリ構成

```
./
├─controller
│  ├─commands // botコマンド群
│  │ │─daily.py // dailyコマンド
│  │ └─status.py // statusコマンド
│  └─events
│    ├─login.py // ログイン処理
│    └─session_events.py // セッション管理処理(VCへの入退室) 
├─data // セッション・ユーザーデータ
│  ├─sessions.db // sqliteDB
│  └─sessions.json // 現在進行中のsessionを管理
├─docs
│  ├db_schema.md // データベース設計 
│  └ER_diagram // ER図
├─domain // Entity
│  ├─basemodel.py // 基底クラス
│  ├─sessions.py // session用Entity
│  └─users.py // user用Entity
├─service
│  ├─service_iinterface.py // サービス用共通interface
│  ├─session_service.py // セッション関連のロジック
│  ├timer_service.py // 作業時間の集計ロジック
│  └user_service.py // ユーザー関連のロジック
├─sql
│  ├─sessions // sessiontableに対して行うsql
│  └─users // usertableに対して行うsql
├─utils // 汎用処理
│  ├─command_loader.py // コマンドの読み込み処理
│  │─event_loader // イベント登録用の処理
│  └─sql_loader.py // tableごとにsqlを読み込む処理
├─bot.py // bot起動時の一連の処理
└─config.py // 環境変数の読み込みなど
```
