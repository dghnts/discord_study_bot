import os

from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()

# 環境変数から読み取り
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
TRACKED_VC_ID = int(os.getenv("TRACKED_VC_ID", 0))  # デフォルト値0

DEBUG = True  # デバッグ用変数
