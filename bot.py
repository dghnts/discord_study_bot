import discord
from discord.ext import commands
from config import TOKEN, TRACKED_VC_ID
from repository.sqlite_storage import SqliteStorage
from timer import TimerService
from controller.event_handler import setup_event_handlers
from controller.command_loader import register_all_commands

# Intents設定
intents = discord.Intents.default()
intents.members = True
intents.voice_states = True
intents.message_content = True

# Botインスタンス作成
bot = commands.Bot(command_prefix="!", intents=intents)

# ストレージとサービス初期化
storage = SqliteStorage()
timer_service = TimerService(storage)

# イベントハンドラ登録
setup_event_handlers(bot, timer_service, TRACKED_VC_ID)

# コマンド登録
register_all_commands(bot, timer_service)

# Bot起動
bot.run(TOKEN)
