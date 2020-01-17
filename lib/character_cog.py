from discord.ext import commands
from lib import character_controller as cc

#コグとして用いるクラス
class CharaCog(commands.Cog):

    #コンストラクタ
    def __init__(self, bot, pc_unique_id):
        self.bot = bot
        self.pc_unique_id = pc_unique_id
        print('setup command $' + pc_unique_id)

    # コマンドグループのルート
    # ${unique_id} に対応
    @command.group(name = pc_unique_id)
    async def root(self, ctx):
        # サブコマンドが呼ばれていない場合、メッセージを表示
        if ctx.invoked_subcommand is None:
            chara = cc.get_chara_data(unique_id)
            await ctx.send( chara['name'] + ' のコマンドっす。\n このコマンドにはサブコマンドが必要っす。')


    # Bot本体側からコグを読み込む際に呼び出される関数。
    def setup(bot):
        bot.add_cog(CharaCog(bot)) # TestCogにBotを渡してインスタンス化し、Botにコグとして登録する。
