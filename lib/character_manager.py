
from lib import character_cog
from collections import OrderedDict

# キャラクタークラスのインスタンスのリスト
# unique_idをkey、Characterオブジェクトをvalueとして持つ順序保証リスト
character_list = OrderedDict()

# 引数で受け取ったcharacterを追加する
# ついでにbotにコグを追加する
def add_character(bot, character):
    character_list[character.unique_id] = character
    bot.add_cog(character_cog.CharaCog(bot, character.unique_id))

# 登録されているunique_idならTrueを返す
def is_register(unique_id):
    if unique_id in character_list:
        return True
    return False

# 単にCharacterインスタンスを返す
def get_character(unique_id):
    print('TODO: [character_controller.py::get_character()] 存在しないunique_idを指定した時のエラーハンドリング')
    return character_list[unique_id]

# キャラクターのステータス値を出力文字列として返す
def status_outputer(unique_id, form):
    chara = get_character(unique_id)
    if form == 'all':
        put_result = ('\nPC名 '+ chara.name +'\n'
                        'ID '+ chara.unique_id +'\n'
                        'STR  '+ chara.get_status_value('STR') +'\n'
                        'CON  '+ chara.get_status_value('CON') +'\n'
                        'POW  '+ chara.get_status_value('POW') +'\n'
                        'DEX  '+ chara.get_status_value('DEX') +'\n'
                        'APP  '+ chara.get_status_value('APP') +'\n'
                        'SIZ  '+ chara.get_status_value('SIZ') +'\n'
                        'INT  '+ chara.get_status_value('INT') +'\n'
                        'EDU  '+ chara.get_status_value('EDU') +'\n'
                        'HP   '+ chara.get_status_value('HP') +'\n'
                        'MP   '+ chara.get_status_value('MP') +'\n'
                        'SAN  '+ chara.get_status_value('SAN') +'\n'
                        'idea '+ chara.get_status_value('idea') +'\n'
                        '幸運  '+ chara.get_status_value('幸運') +'\n'
                        '知識  '+ chara.get_status_value('知識') )

    else:
        status = form
        put_result = ( '\nPC名 '+ chara.name +'\n'+ status + ' ' + chara.get_status_value(status))

    return put_result

# キャラクターの技能値を出力文字列として返す
def skill_outputer(unique_id, skillname):
    chara = get_character(unique_id)
    put_result = ( '\nPC名 '+ chara.name + '\n' + chara.get_skill_name(skillname) + ' ' + chara.get_skill_value(skillname))
    return put_result

# character_listを指定のステータス順にソートし、ソート済みのリストを返す
def sort_by_status(item):
    sorted_character_list = OrderedDict(sorted(character_list.items(), key=lambda  chara:int(chara[1].get_status_value(item)), reverse=True))

    return sorted_character_list

# キャラクターの名前を返す
def get_name(unique_id):
    chara = get_character(unique_id)
    return chara.name

# キャラクターのステータス値のみを返す
def get_status_value(unique_id, status):
    chara = get_character(unique_id)
    return chara.get_status_value(status)

# キャラクターのステータス値を設定する
def set_status_value(unique_id, status, value):
    chara = get_character(unique_id)
    chara.set_status_value(status, value)


# キャラクターの技能値のみを返す
def get_skill_value(unique_id, skillname):
    chara = get_character(unique_id)
    return chara.get_skill_value(skillname)
