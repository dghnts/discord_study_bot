from repository.user_repository import UserRepository


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def register_if_new(self, user_id: str, display_name: str):
        """
        ユーザーが未登録のときのみ、新規登録を行う
        """
        if self.user_repo.get_by_id(user_id) is None:
            self.user_repo.create(user_id, display_name)
