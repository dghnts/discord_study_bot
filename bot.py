import discord
from discord.ext import commands
from config import TOKEN, TRACKED_VC_ID
from study_timer import start_session, end_session

# 必要なintent（メンバーとボイス状態を取得）
intents = discord.Intents.default()
intents.members = True
intents.voice_states = True

# Botインスタンス作成
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅️ Botがログインしました: {bot.user}")

@bot.event
async def on_voice_state_update(member, before, after):
    # ボイスチャンネルの入退室を判定
    if after.channel and after.channel.id == TRACKED_VC_ID:
        # VC二入室
        await start_session(member)
    elif before.channel and before.channel.id == TRACKED_VC_ID and after.channel != before.channel:
        # VCから体質 er 他のチャンネルに移動
        await end_session(member)

# Bot起動
bot.run(TOKEN)