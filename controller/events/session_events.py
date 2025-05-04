import os,json
from datetime import datetime

import discord

from service.user_service import UserService
from service.session_service import SessionService

filepath = "data/sessions.json"

def session_event(bot: discord.Client, tracked_vc_id: int):
    session_service = SessionService()
    user_service: UserService = UserService()

    @bot.event
    async def on_voice_state_update(member, before, after):
        user_id = str(member.id)
        if after.channel and after.channel.id == tracked_vc_id:
            '''セッション開始'''
            """セッション情報を登録する"""
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            """セッション情報を追記"""
            with open(filepath, "r", encoding="utf-8") as f:
                """ファイルの内容を辞書として取得"""
                d = json.load(f)

            if user_id in d.keys():
                print("実行中のセッションがあります")
            else:
                """ 新しいセッセション情報を追記"""
                d[user_id]= {
                    "start_time": str(datetime.now()),
                    "end_time": None,
                    "user_id": user_id,
                    "duration": None
                    }

            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(d, f, indent=2, ensure_ascii=False)
            print(f"{member.display_name} さんが作業開始しました。")

            """セッションの終了"""
        elif before.channel and before.channel.id == tracked_vc_id and (after.channel != before.channel):
            """セッションデータを取得"""
            session_data = get_session_data(user_id)
            if session_data is None:
                print("セッション情報が存在しません")
            else:
                duration = ((datetime.now() - datetime.fromisoformat(session_data["start_time"])) /60).total_seconds()
                session_data["end_time"] = str(datetime.now())
                session_data["duration"] = str(duration)
                '''新規ユーザーの場合、usersDBにユーザー情報を追加'''
                print(member.display_name)
                user_service.add_new_user(user_id, member.display_name)
                '''sessionsDBにセッション情報を登録'''
                session_service.add_new_session(tuple(session_data.values()))

                channel = member.guild.system_channel
                if channel:
                    await channel.send(
                        f"✅ {member.display_name} さんの作業終了\n"
                        f"今回の作業時間：{duration:.1f} 分\n"
                    )
                print(f"{member.display_name} さんの作業終了（{duration:.1f}分） ")

"""現在進行中のセッション情報からユーザーのセッションデータを取得する"""
def get_session_data(user_id: str):
    session_data = None
    with open(filepath, "r", encoding="utf-8") as f:
        """ファイルの内容を辞書として取得"""
        d = json.load(f)
    if user_id in d.keys():
        session_data = d.pop(user_id)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(d, f, indent=2, ensure_ascii=False)

    return session_data