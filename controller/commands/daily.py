from discord.ext import commands

from repository.user_repository import UserRepository
from service.timer_service import TimerService
from service.user_service import UserService


def register(bot: commands.Bot, timer_service: TimerService, user_repo: UserRepository):
    @bot.command(name="daily")
    async def daily(ctx):
        user_service = UserService(user_repo)
        user_id = str(ctx.author.id)
        display_name = ctx.author.display_name

        # ユーザー登録（初回のみ）
        user_service.register_if_new(user_id, display_name)

        # 累積作業時間を取得
        total_minutes = timer_service.get_daily_time_by_user(user_id)

        await ctx.send(f"📊 {display_name} さんの累積作業時間は {total_minutes:.1f} 分です。")
