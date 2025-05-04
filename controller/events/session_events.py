import json
import os
from datetime import datetime

import discord

from domain.session import Session
from repository.session_repository import SessionRepository
from repository.user_repository import UserRepository
from service.session_service import SessionService
from service.user_service import UserService

filepath = "data/sessions.json"


def session_event(bot: discord.Client, session_repo: SessionRepository, user_repo: UserRepository, tracked_vc_id: int):
    session_service = SessionService(session_repo)
    user_service: UserService = UserService(user_repo)

    @bot.event
    async def on_voice_state_update(member, before, after):
        user_id = str(member.id)
        if after.channel and after.channel.id == tracked_vc_id:
            """セッション情報を登録する"""
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            if not os.path.exists(filepath):
                with open(filepath, "w", encoding="utf-8") as f:
                    json.dump({}, f)

            """セッション情報を追記"""
            with open(filepath, "r", encoding="utf-8") as f:
                """ファイルの内容を辞書として取得"""
                d = json.load(f)

            if user_id in d:
                print("実行中のセッションがあります")
            else:
                """ 新しいセッセション情報を追記"""
                d[user_id] = create_session_data(user_id)

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
                session_data["end_time"] = datetime.now().isoformat()
                session = Session.from_dict(session_data)
                # 新規ユーザーの場合、usersDBにユーザー情報を追加
                user_service.register_if_new(user_id, member.display_name)
                # sessionsDBにセッション情報を登録
                session_service.register(session)

                channel = member.guild.system_channel
                if channel:
                    await channel.send(
                        f"✅ {member.display_name} さんの作業終了\n"
                        f"今回の作業時間：{session.duration:.1f} 分\n"
                    )
                print(f"{member.display_name} さんの作業終了（{session.duration:.1f}分） ")


def create_session_data(user_id: str) -> dict:
    session_data = {
        "start_time": str(datetime.now()),
        "end_time": None,
        "user_id": user_id,
        "duration": None
    }
    return session_data


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
