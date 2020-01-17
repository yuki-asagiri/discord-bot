import discord
import asyncio
import traceback
from lib import character_controller as cc
from lib import status_controller as sc
from lib import character_cog
from lib import common_cog
from api_client import dicebot_client as dc
from discord.ext import commands

# OAuthトークンファイルの読み込み
with open('bot-token.txt', 'r') as KEY: secret = KEY.readlines()
token = secret[0].strip()

pc_list = cc.chara_lister()
status_list = ['full', 'STR', 'CON', 'POW', 'DEX', 'APP', 'SIZ', 'INT', 'EDU', 'HP', 'MP', 'SAN', 'idea', '幸運', '知識']


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
        # キャラクターごとのコマンドコグの読み込み
        for unique_id in pc_list:
            try:
                self.add_cog(character_cog.CharaCog(self, unique_id))
            except Exception:
                traceback.print_exc()



# 定義したBotクラスのインスタンス作成と実行
bot = CharaBot(command_prefix='$')
bot.run(token)
