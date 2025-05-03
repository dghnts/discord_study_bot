from discord.ext import commands
from discord import app_commands
import discord

from timer import TimerService


def register(bot: commands.Bot, timer_service):
    @bot.command(name="status")
    async def status(ctx):
        user_id = str(ctx.author.id)
        user = timer_service.get_user_info(user_id)

        if user:
            await ctx.send(f"📊 {ctx.author.display_name} さんの累積作業時間は {user.total_minutes:.1f} 分です。")
        else:
            await ctx.send("⚠️ 作業履歴が見つかりませんでした。")