import discord
from discord.ext import commands
from config import TOKEN, TRACKED_VC_ID
from repository.storage import Storage
from timer import TimerService

# Intents設定
intents = discord.Intents.default()
intents.members = True
intents.voice_states = True

# Botインスタンス作成
bot = commands.Bot(command_prefix="!", intents=intents)

# StorageとService初期化
storage = Storage()
timer_service = TimerService(storage)

@bot.event
async def on_ready():
    print(f"✅ Botがログインしました: {bot.user}")

@bot.event
async def on_voice_state_update(member, before, after):
    # VC入室した場合
    if after.channel and after.channel.id == TRACKED_VC_ID:
        timer_service.start_session(str(member.id), member.display_name)
        print(f"{member.display_name} さんが作業開始しました。")

    # VC退出した場合（別チャンネルに移動を含む）
    elif before.channel and before.channel.id == TRACKED_VC_ID and (after.channel != before.channel):
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

# Bot起動
bot.run(TOKEN)
