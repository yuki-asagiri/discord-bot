from discord.ext import commands
from lib import character_controller as cc

#コグとして用いるクラス
# ${unique_id} とそのサブコマンドを記述
class CharaCog(commands.Cog):

    #コンストラクタ
    def __init__(self, bot, pc_unique_id):
        self.bot = bot
        self.pc_unique_id = pc_unique_id
        # 全コマンドのリスト
        subcommands = self.walk_commands()
        # ルートコマンド
        commands = self.get_commands()
        for c in commands:
            c.update(name = self.pc_unique_id)
        for c in subcommands:
            print(c.qualified_name)

        print('setup command $' + pc_unique_id)

    # コマンドグループのルート
    # ${unique_id} に対応
    @commands.group()
    async def root(self, ctx):
        # サブコマンドが呼ばれていない場合、メッセージを表示
        print('$' + self.pc_unique_id)
        if ctx.invoked_subcommand is None:
            chara = cc.get_chara_data(self.pc_unique_id)
            await ctx.send( chara['name'] + ' のコマンドっす。\n このコマンドにはサブコマンドが必要っす。')

    @root.command()
    async def status(self, ctx, item):
        print('$' + self.pc_unique_id, 'status', item)
        await ctx.send(cc.chara_data_output(self.pc_unique_id, item))
