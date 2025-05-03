from controller.commands import status

def register_all_commands(bot, timer_service):
    status.register(bot, timer_service)
