from controller.commands import status, daily


def register_all_commands(bot, timer_service, user_service):
    status.register(bot, timer_service, user_service)
    daily.register(bot, timer_service, user_service)
