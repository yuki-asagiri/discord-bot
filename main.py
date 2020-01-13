import discord
import asyncio
import file_cont

client = discord.Client()
global read_flag
global oumu_flag
global pc_list
global status_list
global name_flag
global status_flag

name_flag = 'No Chara'
read_flag = 'Off'
oumu_flag = 'Off'
pc_list = file_cont.chara_lister()
status_flag = 'No Status'
status_list = ['STR', 'CON', 'POW', 'DEX', 'APP', 'SIZ', 'INT', 'EDU', 'HP', 'MP', 'SAN', 'idea', '幸運', '知識']

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    global name_flag
    global oumu_flag
    global read_flag
    global pc_list
    global status_list
    if message.author == client.user:
        return

    if oumu_flag == 'On':
        oumu_flag = 'Off'
        await message.channel.send(message.content)

    if '御中くんさよなら' in message.content:
        msg = '皆さんさようならっす'
        oumu_flag = 'Off'
        await message.channel.send(msg)

    if '返事して' in message.content:
        msg = '了解っす'
        oumu_flag = 'On'
        await message.channel.send(msg)

    if 'Hello' in message.content or '御中くんこんにちは':
        print(message.author.name)
        msg = "こんにちはっす" + message.author.name + "さん"
        await message.channel.send(msg)

    if 'ニラレバ' in message.content:
        print('ニラレバ開始')
        msg = "キャラシのURLを貼ってね"
        read_flag = 'On'
        print(read_flag)
        await message.channel.send(msg)

    if 'http' in message.content:
        print('read_flag')
        print(read_flag)
        if read_flag == 'On':
            print('データ読み込み')
            print('success!!')
            chara_url = message.content + '.js'
            print(chara_url)
            chara_data = file_cont.chara_data_download(chara_url)
            print(chara_data)
            ext_chara = file_cont.chara_data_extracter()
            await message.channel.send('以下のキャラデータを保存しました')
            await message.channel.send(file_cont.chara_data_output(ext_chara['name']))
            pc_list.append(ext_chara['name'])
            print(pc_list)
            read_flag = 'Off'

    if file_cont.list_in_message(message.content, pc_list):
        msg = "以下のキャラクターを読み込みました" 
        await message.channel.send(msg)
        print(message.content)
        name_flag = message.content 
        await message.channel.send(file_cont.chara_data_output(message.content, 'full'))

    if file_cont.list_in_message(message.content, status_list) and ':' in message.content:
        msg = "ステータス更新"
        status_flag = message.content.split(':')
        print(status_flag)
        await message.channel.send(msg)
        await message.channel.send(name_flag+'の'+status_flag[0]+'を'+status_flag[1]+'に更新します')
        new_chara_data = file_cont.status_converter(status_flag[0], name_flag, status_flag[1])
        await message.channel.send(file_cont.chara_data_output(name_flag, 'full'))
        name_flag = 'No Chara'
        status_flag = 'No Status'

    if 'ステータス表示' in message.content and file_cont.list_in_message(message.content, status_list):
        status_flag = file_cont.list_in_ob(message.content, status_list)
        msg = name_flag + 'の' + status_flag + 'を表示します'
        await message.channel.send(file_cont.chara_data_output(name_flag, status_flag))
        status_flag = 'No Status'

client.run("NjY1ODA4MTAxOTUzNTAzMjQy.XhrAZQ.JXE6A5bE5eRMfwqN6MgrufuXWHI")

