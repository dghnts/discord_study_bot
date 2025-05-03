import discord

from service.session_service import SessionService

def login_event(bot: discord.Client):
    @bot.event
    async def on_ready():
        print(f"✅ Botがログインしました: {bot.user}")
