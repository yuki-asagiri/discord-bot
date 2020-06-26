import discord
import asyncio
import traceback
from collections import OrderedDict
from lib import character_manager as cm
from lib import session_manager as sm
from lib import character_cog
from api_client import dicebot_client as dc
from discord.ext import commands

#listコマンド内でCharacterクラスを扱っちゃってるのはやめたいね

# コグとして用いるクラス
# 一般的なコマンドを記述
class CommonCog(commands.Cog):

    #コンストラクタ
    def __init__(self, bot):
        self.bot = bot
        print('setup common commands.')

    #コマンド処理
    @commands.command()
    async def test(self, ctx):
        print('/test')
        await ctx.send('ひえー')

    @commands.group()
    async def session(self, ctx):
        if ctx.invoked_subcommand is None:
            print('/session')
            await ctx.send('サブコマンドが必要です。\n/session begin を実行した場合、' + ctx.channel.name + 'という名前のセッションが新たに生成されます。')

    @session.command()
    async def make(self, ctx, title):
        await ctx.send('シナリオ用のデータが作成される予定だけど未実装っすよ')

    @session.command()
    async def load(self, ctx, title):
        await ctx.send('シナリオ用のデータが読み込まれる予定だけど未実装っすよ')

    @session.command()
    async def list(self, ctx):
        await ctx.send('シナリオの一覧が表示される予定だけど未実装っすよ')


    @commands.command()
    async def load(self, ctx, unique_id, url):
        print('/load', unique_id, url)
        chara_dl_bool = sm.add_character(self.bot, unique_id, url + '.json')

        if chara_dl_bool:
            print('/load success')
        else:
            print('/load failure')

    @commands.command()
    async def list(self, ctx, command):
        print('/list', command)
        # コマンドの分岐
        # ステータス指定 → そのステータスのみ表示
        # 'battle' → DEX, HP, MP, SAN
        if command == 'battle':
            # DEX順ソートした上で、諸々の情報表示
            sorted_character_list = cm.sort_by_status('DEX')
            message = '戦闘用リスト\n'
            for character in sorted_character_list.values():
                message = message + character.name + ' | DEX: ' + character.get_status_value('DEX') + ' | HP: ' + character.get_status_value('HP') + '/' + character.get_status_value('MAXHP') + ' | MP: ' + character.get_status_value('MP') + '/' + character.get_status_value('MAXMP') + ' | SAN: ' + character.get_status_value('SAN') + '\n'
            await ctx.send(message)

        else:
            sorted_character_list = cm.sort_by_status(command)
            message = command + '順ソート\n'
            for character in sorted_character_list.values():
                message = message + cm.status_outputer(character.unique_id, command) + '\n'
            await ctx.send(message)
