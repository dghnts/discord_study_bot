import json
from datetime import datetime
import os
from sys import displayhook

from config import DEBUG

# 保存先パス
DATA_PATH = "data/sessions.json"

# 現在動いているセッション
active_sessions = dict()

# セッションデータの読み込み
def _load_data():
    # セッションデータが存在するか確認
    if not os.path.exists(DATA_PATH):
        return {}
    # 存在する場合jsonとして読み込む
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

# データの保存
def _save_data(data):
    # DATA_PATH当名前のディレクトリを作成する
    # 既にディレクトリが存在している場合はスルー
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    # ディレクトリ内のファイルにデータを保存する
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# セッションを開始する
async def start_session(member):
    user_id = str(member.id)
    # セッションをスタートしたユーザー情報がまだ登録されていない場合
    if user_id not in active_sessions:
        # 現在時刻をユーザーの作業開始時刻として登録
        active_sessions[user_id]= {
            "start": datetime.now().isoformat(),
            "display_name": member.display_name
        }
# セッションの終了を記録する
async def end_session(member):
    user_id = str(member.id)
    # ユーザー情報がsession情報に保存されている場合
    if user_id in active_sessions:
        # セッションの開始時刻を取得する（取得後セッション情報から削除）
        start_time = datetime.fromisoformat(active_sessions.pop(user_id))
        # 現在の時刻を酋長時刻として取得
        end_time = datetime.now()
        # 作業時間を計算
        duration = (end_time-start_time).total_seconds() / 60 # 分単位

        # セッションファイルの読み込み/更新
        data = _load_data()

        if user_id not in data:
            data[user_id] = {
                "display_name": member.display_name,
                "total_minutes": 0.0,
                "sessions": []
            }

        data[user_id]["sessions"] = data.get(user_id, 0) + duration
        _save_data(data)

        # 作業終了メッセージ
        channel = member.guild.system_channel
        if channel:
            message = (f"✅ {member.display_name} さんの作業終了\n "
                       f"今回の作業時間：{duration:.1f} 分\n ")
            if(DEBUG):
                print(message)
            else:
                await channel.send(message)


