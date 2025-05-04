import discord
from discord.ext import commands
from config import TOKEN, TRACKED_VC_ID
from service.session_service import SessionService
from service.user_service import UserService
from service.timer_service import TimerService
from utils.event_loader import register_all_events
from utils.command_loader import register_all_commands
from utils.event_loader import register_all_events

# Intents設定
intents = discord.Intents.default()
intents.members = True
intents.voice_states = True
intents.message_content = True

# Botインスタンス作成
bot = commands.Bot(command_prefix="!", intents=intents)

# イベントハンドラ登録
register_all_events(bot, TRACKED_VC_ID)

# コマンド登録
#register_all_commands(bot, timer_service, user_service)

# Bot起動
bot.run(TOKEN)
