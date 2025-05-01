import discord
from discord.ext import commands
from config import TOKEN, TRACKED_VC_ID
from repository.storage import Storage
from timer import TimerService
from controller.event_handler import setup_event_handlers

# Intents設定
intents = discord.Intents.default()
intents.members = True
intents.voice_states = True

# Botインスタンス作成
bot = commands.Bot(command_prefix="!", intents=intents)

# ストレージとサービス初期化
storage = Storage()
timer_service = TimerService(storage)

# イベントハンドラ登録
setup_event_handlers(bot, timer_service, TRACKED_VC_ID)

# Bot起動
bot.run(TOKEN)
