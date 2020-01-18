import requests
import glob
import json
import os
import traceback
from lib import file_controller as fc
from lib import chara_json_handler as cjh

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

def chara_lister():
    dir_path = 'path/chara_data/'
    file_list = glob.glob(dir_path+'*')
    pc_name_list = []
    for file_name in file_list:
       pc_name_list.append(file_name.split('.')[0].split('/')[2])
    print(pc_name_list)

    return pc_name_list

# 一時ファイルの作成及びキャラデータリクエスト
def chara_data_download(id_url, unique_id):
    print('downloaderの読み込み')
    headers = {"content-type": "application/json"}
    req = id_url
    response = requests.get(req, headers=headers)
    try:
        data = response.json()
        print(data)
        # jsonのフォーマットを整形する
        chara_data_extracter(data, unique_id)
        result = True
    except Exception:
        traceback.print_exc()
        result = False
    return result

def chara_data_extracter(chara, unique_id):
    print('キャラデータの保存')

    # 基礎ステータスの読み込み
    new_chara_json = cjh.convert_hokanjo_format_to_charajson(chara, unique_id)

    # キャラデータの保存
    print('Chara_data save now')
    fc.file_writer(new_chara_json, unique_id)

# 単にキャラデータのjsonだけを返す
def get_chara_data(unique_id):
    return fc.file_reader(unique_id)

def chara_data_output(unique_id, form):
    chara_data = fc.file_reader(unique_id)
    return status_outputer(chara_data, form)

def status_outputer(data, form):
    if form == 'all':
        put_result = ('\nPC名 '+data['name']+'\n'
                        'ID '+data['unique_id']+'\n'
                        'STR  '+data['status']['STR']+'\n'
                        'CON  '+data['status']['CON']+'\n'
                        'POW  '+data['status']['POW']+'\n'
                        'DEX  '+data['status']['DEX']+'\n'
                        'APP  '+data['status']['APP']+'\n'
                        'SIZ  '+data['status']['SIZ']+'\n'
                        'INT  '+data['status']['INT']+'\n'
                        'EDU  '+data['status']['EDU']+'\n'
                        'HP   '+data['status']['HP']+'\n'
                        'MP   '+data['status']['MP']+'\n'
                        'SAN  '+data['status']['SAN']+'\n'
                        'idea '+data['status']['idea']+'\n'
                        '幸運 '+data['status']['幸運']+'\n'
                        '知識 '+data['status']['知識'])

    else:
        status = form
        put_result = ( '\nPC名 '+data['name']+'\n'+status + ' ' + data['status'][form])
    print(put_result)

    return put_result

def get_status_value(unique_id, form):
    chara_data = fc.file_reader(unique_id)
    return chara_data['status'][form]

def skill_data_output(unique_id, skillname):
    chara_data = fc.file_reader(unique_id)
    return skill_outputer(chara_data, skillname)

def skill_outputer(data, skill):
    put_result = ( '\nPC名 '+data['name']+'\n'+data['skill'][skill]['name'] + ' ' + data['skill'][skill]['value'])
    print(put_result)
    return put_result

def get_skill_value(unique_id, skillname):
    chara_data = fc.file_reader(unique_id)
    return chara_data['skill'][skillname]['value']

if __name__ == '__main__':
    test()

print('success status controller load')
