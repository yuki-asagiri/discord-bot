import discord
import asyncio
import traceback
from lib import character_controller as cc
from lib import status_controller as sc
from api_client import dicebot_client as dc
from discord.ext import commands

# OAuthトークンファイルの読み込み
with open('bot-token.txt', 'r') as KEY: secret = KEY.readlines()
token = secret[0].strip()

# 変数定義
oumu_flag = False
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

        # キャラクターごとのcogコマンドの用意
        for unique_id in pc_list:
            try:
                self.load_extension(unique_id)
            except Exeption:
                traceback.print_exc()


        # メッセージに対する反応集
    @bot.event
    async def on_message(message):
        global oumu_flag
        print(message.author.name)

        if message.author.bot:
            return

        if '返事やめて' in message.content:
            msg = '了解っす。'
            oumu_flag = False
            await message.channel.send(msg)

        if oumu_flag:
            await message.channel.send(message.content+'、っす。')

        if '返事して' in message.content:
            msg = '了解っす。'
            oumu_flag = True
            await message.channel.send(msg)

        if dc.string_analyze(message.content):
            msg = dc.dice_api_client(message.content)
            print(msg[0])
            dm = await message.author.create_dm()
            await message.channel.send(msg[0])
            if msg[1]:
                await dm.send(msg[0])
        else:
            await bot.process_commands(message)

    #コマンド処理
    @bot.command()
    async def test(ctx):
        print('$test')
        await ctx.send('ひえー')

    @bot.command()
    async def load(ctx, unique_id, url):
        print('$load', unique_id, url)
        if url == '':
            await ctx.send('urlを入力してくださいっす。')
            return

        # キャラクター保管所からデータを持ってくる
        chara_url = url + '.js'
        chara_dl_bool = cc.chara_data_download(chara_url, unique_id)
        print(chara_dl_bool)
        if chara_dl_bool:
            print('success!!')
            if cc.list_in_chara(unique_id, pc_list):
                print('The '+ unique_id + ' is overwritten')
                await ctx.send(unique_id + 'さんのデータは上書きされるっす。')
            else:
                pc_list.append(unique_id)
                await ctx.send('以下のキャラデータを保存したっすよ。')
                await ctx.send(cc.chara_data_output(unique_id, 'all'))
                self.load_extension(unique_id)
        else:
            await ctx.send('キャラクターを読み込めなかったっす。')
        print(pc_list)

    @bot.command()
    async def show(ctx, unique_id, item):
        print('$show', unique_id, item)
        await ctx.send(cc.chara_data_output(unique_id, item))

    # skillコマンドは仮実装（実際はshowコマンドにぶら下げたい）
    @bot.command()
    async def skill(ctx, unique_id, skillname):
        print('$skill', unique_id, skillname)
        await ctx.send(cc.skill_data_output(unique_id, skillname))

    # updateコマンドは現時点では増減指定のみ対応
    @bot.command()
    async def update(ctx, unique_id, item, amount):
        print('$update', unique_id, item, amount)
        if(sc.is_initial_sign(amount)):
            sc.status_converter2(item, unique_id, amount)
        else:
            sc.status_converter(item, unique_id, amount)
        await ctx.send(cc.chara_data_output(unique_id, item))

# 定義したBotクラスのインスタンス作成と実行
bot = CharaBot(command_prefix='$')
bot.run(token)
