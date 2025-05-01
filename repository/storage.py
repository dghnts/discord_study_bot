import json
import os
from datetime import datetime

from domain.session import Session
from domain.user import User


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
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                raw_data = json.load(f)
                self.users = {
                    user_id: User.from_dict(user_id, user_data)
                    for user_id, user_data in raw_data.items()
                }
        except (json.JSONDecodeError, TypeError) as e:
            print(f"⚠️ sessions.jsonの読み込みに失敗しました（ファイル破損など）: {e}")
            self.users = {}
        except Exception as e:
            print(f"⚠️ sessions.jsonの読み込み中に予期せぬエラー: {e}")
            self.users = {}

    def _save(self):
        """現在のデータをファイルに保存"""
        try:
            os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
            with open(self.filepath, "w", encoding="utf-8") as f:
                data = {user_id: user.to_dict() for user_id, user in self.users.items()}
                json.dump(data, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"⚠️ sessions.jsonの保存に失敗しました: {e}")
        except Exception as e:
            print(f"⚠️ 予期せぬ保存エラー: {e}")

    def start_session(self, user_id: str, display_name: str):
        """セッション開始（開始時間を一時的に記憶）"""
        if user_id not in self.users:
            self.users[user_id] = User(user_id, display_name)
        self.users[user_id].current_start_time = datetime.now()

    def end_session(self, user_id: str, display_name: str):
        """セッション終了（セッション作成・保存）"""
        user = self.users.get(user_id)
        if user is None:
            print(f"⚠️ セッション終了要求: 未登録のユーザー {user_id}")
            return None, None

        if not hasattr(user, 'current_start_time'):
            print(f"⚠️ セッション未開始のまま終了しようとしました（{user.display_name}）")
            return None, None
        try:
            session = Session(user.current_start_time, datetime.now())
            user.add_session(session)
            user.display_name = display_name
            del user.current_start_time
            self._save()
            return session.duration, user.total_minutes
        except Exception as e:
            print(f"⚠️ セッション終了処理中にエラーが発生しました: {e}")
            return None, None


    def get_user(self, user_id: str):
        """特定ユーザー情報を取得（存在しない場合はNone）"""
        return self.users.get(user_id)


    def get_all_users(self):
        """すべてのユーザー情報をリストで取得"""
        return list(self.users.values())
