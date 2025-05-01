import discord
from timer import TimerService

def setup_event_handlers(bot: discord.Client, timer_service: TimerService, tracked_vc_id: int):
    @bot.event
    async def on_ready():
        print(f"✅ Botがログインしました: {bot.user}")

    @bot.event
    async def on_voice_state_update(member, before, after):
        if after.channel and after.channel.id == tracked_vc_id:
            timer_service.start_session(str(member.id), member.display_name)
            print(f"{member.display_name} さんが作業開始しました。")

        elif before.channel and before.channel.id == tracked_vc_id and (after.channel != before.channel):
            duration, total_minutes = timer_service.end_session(str(member.id), member.display_name)
            if duration is not None:
                channel = member.guild.system_channel
                if channel:
                    await channel.send(
                        f"✅ {member.display_name} さんの作業終了\n"
                        f"今回の作業時間：{duration:.1f} 分\n"
                        f"累積作業時間：{total_minutes:.1f} 分"
                    )
                print(f"{member.display_name} さんの作業終了（{duration:.1f}分） 累積：{total_minutes:.1f}分")
