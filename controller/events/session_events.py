from datetime import datetime

import discord

from service.user_service import UserService
from service.session_service import SessionService

def session_event(bot: discord.Client, tracked_vc_id: int):
    session_service = SessionService()
    user_service = UserService()

    @bot.event
    async def on_voice_state_update(member, before, after):
        if after.channel and after.channel.id == tracked_vc_id:
            '''セッション開始'''
            '''新規ユーザーの場合、usersDBにユーザー情報を追加'''
            user_service.add_new_user(str(member.id), member.display_name)
            '''sessionsDBにセッション情報を登録'''
            session_service.add_new_session(str(member.id))
            print(f"{member.display_name} さんが作業開始しました。")

        elif before.channel and before.channel.id == tracked_vc_id and (after.channel != before.channel):
            """セッションの終了"""
            """現在のセッションを取得"""
            session = session_service.get_current_session(str(member.id))
            """終了時刻と作業時間を追加"""
            duration = session_service.add_end_time(session)

            if duration is not None:
                channel = member.guild.system_channel
                if channel:
                    await channel.send(
                        f"✅ {member.display_name} さんの作業終了\n"
                        f"今回の作業時間：{duration:.1f} 分\n"
                    )
                print(f"{member.display_name} さんの作業終了（{duration:.1f}分） ")