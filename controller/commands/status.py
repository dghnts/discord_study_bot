from discord.ext import commands
from utils.total_minutes import total_minutes
def register(bot: commands.Bot, user_service):
    @bot.command(name="status")
    async def status(ctx):
        user_id = str(ctx.author.id)
        user = user_service.get_user_info(user_id)

        if user:
            await ctx.send(f"📊 {ctx.author.display_name} さんの累積作業時間は  分です。")
        else:
            await ctx.send("⚠️ 作業履歴が見つかりませんでした。")