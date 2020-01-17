from discord.ext import commands
from lib import character_controller as cc
from api_client import dicebot_client as dc
from lib import status_controller as sc

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

    # ステータス増減
    @commands.command()
    async def update(self, ctx, item, amount):
        print('$' + self.pc_unique_id, 'update', item, amount)

        before = cc.get_status_value(self.pc_unique_id, item)
        if(sc.is_initial_sign(amount)):
            sc.status_converter2(item, self.pc_unique_id, amount)
        else:
            sc.status_converter(item, self.pc_unique_id, amount)
        after = cc.get_status_value(self.pc_unique_id, item)
        data = cc.get_chara_data(self.pc_unique_id)

        await ctx.send('\nPC名 '+data['name']+'\n'+item + ' ' + before + ' → ' + after)

    # スキルロール
    @commands.command()
    async def roll(self, ctx, skillname):
        print('$' + self.pc_unique_id, 'roll', skillname)
        # まずは技能値を表示
        await ctx.send(cc.skill_data_output(self.pc_unique_id, skillname))
        # 次にダイスロール実施
        skill_value = cc.get_skill_value(self.pc_unique_id, skillname)
        msg = dc.dice_api_client('ccb<=' + skill_value)
        print(msg[0])
        dm = await ctx.author.create_dm()
        await ctx.send(msg[0])
        if msg[1]:
            await dm.send(msg[0])

    # スキルロール
    @commands.command()
    async def sroll(self, ctx, skillname):
        print('$' + self.pc_unique_id, 'roll', skillname)
        # まずは技能値を表示
        await ctx.send(cc.skill_data_output(self.pc_unique_id, skillname) + '　［シークレットダイス］')
        # 次にダイスロール実施
        skill_value = cc.get_skill_value(self.pc_unique_id, skillname)
        msg = dc.dice_api_client('sccb<=' + skill_value)
        print(msg[0])
        dm = await ctx.author.create_dm()
        await ctx.send(msg[0])
        if msg[1]:
            await dm.send(msg[0])
