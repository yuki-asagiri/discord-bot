import requests
import glob
import json
import os
import traceback
from lib import file_controller as fc
from lib import character

character_list = {}

def test():
    print('キャラデータの操作ファイルです')

def list_in_keyword(keyword, lolist):
    for i in lolist:
        if i in keyword:
            return True

def list_in_chara(chara, lolist):
    for i in lolist:
        if chara == i:
            return i

def chara_loader(unique_id):
    return fc.file_reader(unique_id)

def chara_saver(character_json, unique_id):
    return fc.file_writer(character_json, unique_id)

# キャラクターのステータスデータ読み込み、およびキャラ名のリスト作成
def chara_lister():
    print('TODO: [character_controller.py::chara_lister()] 関数の場所移動を検討。') # ファイル名から登録済みunique_idのリストを作っているだけなのでこのまま再利用可能想定
    dir_path = 'path/chara_data/'
    file_list = glob.glob(dir_path+'*')
    pc_name_list = []
    for file_name in file_list:
        unique_id = file_name.split('.')[0].split('/')[2]
        character_list[unique_id] = fc.file_reader(unique_id)
        pc_name_list.append(unique_id)
    print(pc_name_list)

    return pc_name_list

# キャラデータリクエストおよびCharacterインスタンスの作成、リストへの追加
def chara_data_download(id_url, unique_id):
    print('downloaderの読み込み')
    print('TODO: [character_controller.py::chara_data_downloader] キャラ周りの再構成に伴い、本メソッドの移動を検討')
    headers = {"content-type": "application/json"}
    req = id_url
    response = requests.get(req, headers=headers)
    try:
        data = response.json()
        # print(data) 流石にログが煩いのでコメントアウト
        # Characterクラスのインスタンスを作成、格納
        character_list[unique_id] = character.Character(unique_id, data)
        result = True
    except Exception:
        traceback.print_exc()
        result = False
    return result

# 使用しなくなる想定
def chara_data_extracter(chara, unique_id):
    print('TODO: [character_controller.py::chara_data_extracter()] 本メソッドは未使用となる想定')
    print('キャラデータの保存')

    # 基礎ステータスの読み込み
    new_chara_json = cjh.convert_hokanjo_format_to_charajson(chara, unique_id)

    # キャラデータの保存
    print('Chara_data save now')
    fc.file_writer(new_chara_json, unique_id)

# 単にCharacterインスタンスを返す
def get_character(unique_id):
    print('TODO: [character_controller.py::get_character()] 存在しないunique_idを指定した時のエラーハンドリング')
    return character_list[unique_id]

# キャラクターデータを出力する
def chara_data_output(unique_id, form):
    print('TODO: [character_controller.py::chara_data_output()] status_outputer()と統合していい可能性がある')
    return status_outputer(unique_id, form)

def status_outputer(unique_id, form):
    chara = get_character(unique_id)
    if form == 'all':
        put_result = ('\nPC名 '+ chara.get_name() +'\n'
                        'ID '+ chara.get_unique_id() +'\n'
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
        put_result = ( '\nPC名 '+ chara.get_name() +'\n'+ status + ' ' + chara.get_status_value(form))
    print(put_result)

    return put_result

def get_status_value(unique_id, form):
    chara = get_character(unique_id)
    return chara.get_status_value(form)

def skill_data_output(unique_id, skillname):
    print('TODO: [character_controller.py::skill_data_output()] skill_outputerと統合して良い可能性がある')
    return skill_outputer(unique_id, skillname)

def skill_outputer(unique_id, skillname):
    chara = get_character(unique_id)
    put_result = ( '\nPC名 '+ chara.get_name() + '\n' + chara.get_skill_name(skillname) + ' ' + chara.get_skill_value(skillname))
    print(put_result)
    return put_result

def get_skill_value(unique_id, skillname):
    chara = get_character(unique_id)
    return chara.get_skill_value(skillname)

if __name__ == '__main__':
    test()

print('success status controller load')
