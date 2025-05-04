import discord
from discord.ext import commands

from config import TOKEN, TRACKED_VC_ID
from repository.session_repository import SessionRepository
from repository.user_repository import UserRepository
from service.timer_service import TimerService
from utils.command_loader import register_all_commands
from utils.event_loader import register_all_events

# Intents設定
intents = discord.Intents.default()
intents.members = True
intents.voice_states = True
intents.message_content = True

# Botインスタンス作成
bot = commands.Bot(command_prefix="!", intents=intents)

session_repo = SessionRepository()
user_repo = UserRepository()
timer_service = TimerService(session_repo)

# イベントハンドラ登録
register_all_events(bot, session_repo, user_repo, TRACKED_VC_ID)

# コマンド登録
register_all_commands(bot, timer_service, user_repo)

# Bot起動
bot.run(TOKEN)
