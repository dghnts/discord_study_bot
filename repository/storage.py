import os
import json
from domain.user import User
from domain.session import Session
from datetime import datetime

class Storage:
    def __init__(self, filepath="data/sessions.json"):
        self.filepath = filepath
        self.users = {}  # Dict[str, User]
        self._load()

    def _load(self):
        """ファイルからデータを読み込み"""
        if not os.path.exists(self.filepath):
            self.users = {}
            return
        with open(self.filepath, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
            self.users = {
                user_id: User.from_dict(user_id, user_data)
                for user_id, user_data in raw_data.items()
            }

    def _save(self):
        """現在のデータをファイルに保存"""
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        with open(self.filepath, "w", encoding="utf-8") as f:
            data = {user_id: user.to_dict() for user_id, user in self.users.items()}
            json.dump(data, f, indent=2, ensure_ascii=False)

    def start_session(self, user_id: str, display_name: str):
        """セッション開始（開始時間を一時的に記憶）"""
        if user_id not in self.users:
            self.users[user_id] = User(user_id, display_name)
        self.users[user_id].current_start_time = datetime.now()

    def end_session(self, user_id: str, display_name: str):
        """セッション終了（セッション作成・保存）"""
        user = self.users.get(user_id)
        if user and hasattr(user, 'current_start_time'):
            session = Session(user.current_start_time, datetime.now())
            user.add_session(session)
            user.display_name = display_name  # 最新の表示名で更新
            del user.current_start_time  # セッション開始時刻をクリア
            self._save()
            return session.duration, user.total_minutes
        return None, None

    def get_user(self, user_id: str):
        """特定ユーザー情報を取得（存在しない場合はNone）"""
        return self.users.get(user_id)

    def get_all_users(self):
        """すべてのユーザー情報をリストで取得"""
        return list(self.users.values())
