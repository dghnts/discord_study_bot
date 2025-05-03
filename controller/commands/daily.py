from discord.ext import commands


def register(bot: commands.Bot, timer_service, user_service):
    @bot.command(name="daily")
    async def daily(ctx):
        user_id = str(ctx.author.id)
        minutes = timer_service.get_today_minutes(user_id)

        await ctx.send(f"📊 今日の作業時間は {minutes:.1f} 分です。")
