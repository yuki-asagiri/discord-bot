import discord
import asyncio
import file_cont
import cocutil

from discord.ext import commands

pc_list = file_cont.chara_lister()
status_list = ['full', 'STR', 'CON', 'POW', 'DEX', 'APP', 'SIZ', 'INT', 'EDU', 'HP', 'MP', 'SAN', 'idea', '幸運', '知識']

#コマンド関連の定義
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

#コマンド処理
@bot.command()
async def test(ctx):
    print('$test')
    await ctx.send('ひえー')

@bot.command()
async def load(ctx, unique_id, url):
    print('$load', unique_id, url)

    chara_url = url + '.js'
    raw_chara_data = file_cont.chara_data_download(chara_url)
    print(raw_chara_data)
    chara_data = file_cont.chara_data_extracter(unique_id)
    await ctx.send('以下のキャラデータを保存しました')
    await ctx.send(file_cont.chara_data_output(unique_id, 'full'))
    print('success!!')
    pc_list.append(unique_id)
    print(pc_list)

@bot.command()
async def show(ctx, unique_id, item):
    print('$show', unique_id, item)
    await ctx.send(file_cont.chara_data_output(unique_id, item))

# updateコマンドは現時点では増減指定のみ対応
@bot.command()
async def update(ctx, unique_id, item, amount):
    print('$update', unique_id, item, amount)
    if(cocutil.is_initial_sign(amount)):
        new_chara_data = file_cont.status_converter2(item, unique_id, amount)
    else:
        new_chara_data = file_cont.status_converter(item, unique_id, amount)
    await ctx.send(file_cont.chara_data_output(unique_id, item))

bot.run("")
