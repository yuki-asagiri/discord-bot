from discord.ext import commands
from lib import character_controller as cc
from api_client import dicebot_client as dc

# ルートコマンドの名前を変更すると、ぶら下げていたサブコマンドが全て無になってしまう仕様？らしい
# サブコマンドを手動で登録することによって気合で解決しているが、現状ではサブコマンドは1階層まで。
# つまり、 ${unique_id} {サブコマンド1} 引数...
# という形のコマンドのみ可
# とりあえず足りそうなので妥協した。

#コグとして用いるクラス
# ${unique_id} とそのサブコマンドを記述
class CharaCog(commands.Cog):
    #コンストラクタ
    def __init__(self, bot, pc_unique_id):
        self.bot = bot
        self.pc_unique_id = pc_unique_id
        # ルートコマンド
        commands = self.get_commands()
        for c in commands:
            if c.name == 'root':
                root_command = c
                c.update(name = self.pc_unique_id)
            else:
                root_command.add_command(c)

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

    # 以下、あとで手動でサブコマンド化するので、サブコマンドはcommands.command()でデコレートする。
    # ステータス表示
    @commands.command()
    async def status(self, ctx, item):
        print('$' + self.pc_unique_id, 'status', item)
        await ctx.send(cc.chara_data_output(self.pc_unique_id, item))

    # スキル表示
    @commands.command()
    async def skill(self, ctx, skillname):
        print('$' + self.pc_unique_id, 'skill', skillname)
        await ctx.send(cc.skill_data_output(self.pc_unique_id, skillname))

    # スキルロール
    @commands.command(alias = 'dice')
    async def roll(self, ctx, skillname):
        print('$' + self.pc_unique_id, 'roll', skillname)
        # まずは技能値を表示
        await ctx.send(cc.skill_data_output(self.pc_unique_id, skillname))
        # 次にダイスロール実施
        skill_value = cc.get_skill_value(self.pc_unique_id, skillname)
        msg = dc.dice_api_client('ccb<=' + skill_value)
        print(msg[0])
        dm = await message.author.create_dm()
        await message.channel.send(msg[0])
        if msg[1]:
            await dm.send(msg[0])
