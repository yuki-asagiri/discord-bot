import discord
import asyncio
import traceback
from lib import common_cog
from api_client import dicebot_client as dc
from discord.ext import commands

# OAuthトークンファイルの読み込み
with open('bot-token.txt', 'r') as KEY: secret = KEY.readlines()
token = secret[0].strip()

# Botクラス
class CharaBot(commands.Bot):
    # コンストラクタ
    def __init__(self, command_prefix):
        # スーパークラスのコンストラクタ
        super().__init__(command_prefix)

    # ログイン時の処理
    async def on_ready(self):
        # ログイン情報
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

        # 一般的なコマンドコグの読み込み
        self.add_cog(common_cog.CommonCog(self))

# 定義したBotクラスのインスタンス作成と実行
bot = CharaBot(command_prefix='/')
bot.run(token)
