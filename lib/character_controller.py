import requests
import glob
import json
import urllib.request
import os
from lib import file_controller as fc

def test():
    print('キャラデータの操作ファイルです')

def list_in_keyword(keyword, lolist):
    for i in lolist:
        if i in keyword:
            return True

def list_in_ob(message, lolist):
    for i in lolist:
        if i in message:
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
    dir_path = 'path/chara_data/'
    tmp_id = 'malmalmalmal'
    file_name = dir_path + tmp_id + '.json'
    # chara_id = 'path/chara_data/malmalmalmal.json'

    # return urllib.request.urlretrieve(id_url, chara_id)
    response = requests.get(id_url)
    print(response)
    raw_chara_data = urllib.request.urlretrieve(id_url, file_name)
    print(raw_chara_data)
    if raw_chara_data =='undefined':
        print('Error occured. Can not load json data')
        return 'キャラデータを読み込めませんでした'
    else:
        print('Chara load success')

    # jsonのフォーマットを整形する
    chara_data = chara_data_extracter(unique_id)

    return chara_data

def chara_data_extracter(unique_id):
    print('キャラデータの保存')

    # tmpデータのID
    tmp_id = 'malmalmalmal'

    # 一時ファイルの読み込み
    chara = fc.file_reader(tmp_id)

    # 基礎ステータスの読み込み
    new_chara_json = { "name" : chara["pc_name"],
      "unique_id" : unique_id,
      "status" : {
          "STR"  : chara["NA1"],
          "CON"  : chara["NA2"],
          "POW"  : chara["NA3"],
          "DEX"  : chara["NA4"],
          "APP"  : chara["NA5"],
          "SIZ"  : chara["NA6"],
          "INT"  : chara["NA7"],
          "EDU"  : chara["NA8"],
          "HP"   : chara["NA9"],
          "MP"   : chara["NA10"],
          "SAN"  : chara["NA11"],
          "idea" : chara["NA12"],
          "幸運" : chara["NA13"],
          "知識" : chara["NA14"]
        },
      # 戦闘系技能：TBAP、探索系技能：TFAP 行動系技能：TAAP 交渉系技能：TCAP 知識系技能:TLAP
      "skill" : {
          "回避" :
            {"name" : "回避",
             "value" : chara["TBAP"][0]},
          "キック" :
            {"name" : "キック",
             "value" : chara["TBAP"][1]},
          "組み付き" :
            {"name" : "組み付き",
             "value" : chara["TBAP"][2]},
          "パンチ" :
            {"name" : "パンチ",
             "value" : chara["TBAP"][3]},
          "頭突き" :
            {"name" : "頭突き",
             "value" : chara["TBAP"][4]},
          "投擲" :
            {"name" : "投擲",
             "value" : chara["TBAP"][5]},
          "マーシャルアーツ" :
            {"name" : "マーシャルアーツ",
             "value" : chara["TBAP"][6]},
          "拳銃" :
            {"name" : "拳銃",
             "value" : chara["TBAP"][7]},
          "サブマシンガン" :
            {"name" : "サブマンガン",
             "value" : chara["TBAP"][8]},
          "ショットガン" :
            {"name" : "ショットガン",
             "value" : chara["TBAP"][9]},
          "マシンガン" :
            {"name" : "マシンガン",
             "value" : chara["TBAP"][10]},
          "ライフル" :
           {"name" : "ライフル",
            "value" : chara["TBAP"][11]},
          # 戦闘系技能で独自のものを追加した場合ここに入る可能性がある（未対応）

          "応急手当" :
            {"name" : "応急手当",
             "value" : chara["TFAP"][0]},
          "鍵開け" :
            {"name" : "鍵開け",
             "value" : chara["TFAP"][1]},
          "隠す" :
            {"name" : "隠す",
             "value" : chara["TFAP"][2]},
          "隠れる" :
            {"name" : "隠れる",
             "value" : chara["TFAP"][3]},
          "聞き耳" :
            {"name" : "聞き耳",
             "value" : chara["TFAP"][4]},
          "忍び歩き" :
            {"name" : "忍び歩き",
             "value" : chara["TFAP"][5]},
          "写真術" :
            {"name" : "写真術",
             "value" : chara["TFAP"][6]},
          "精神分析" :
            {"name" : "精神分析",
             "value" : chara["TFAP"][7]},
          "追跡" :
            {"name" : "追跡",
             "value" : chara["TFAP"][8]},
          "登攀" :
            {"name" : "登攀",
             "value" : chara["TFAP"][9]},
          "図書館" :
            {"name" : "図書館",
             "value" : chara["TFAP"][10]},
          "目星" :
            {"name" : "目星",
             "value" : chara["TFAP"][11]},
          #探索系技能で独自のものを追加した場合ここに入る可能性がある（未対応）

          "運転" :
            {"name" : "運転（" + chara["unten_bunya"] + "）",
             "value" : chara["TAAP"][0]},
          "機械修理" :
            {"name" : "機械修理",
             "value" : chara["TAAP"][1]},
          "重機械操作" :
            {"name" : "重機械操作",
             "value" : chara["TAAP"][2]},
          "乗馬" :
            {"name" : "乗馬",
             "value" : chara["TAAP"][3]},
          "水泳" :
            {"name" : "水泳",
             "value" : chara["TAAP"][4]},
          "製作" :
            {"name" : "制作（" + chara["seisaku_bunya"] + "）",
             "value" : chara["TAAP"][5]},
          "操縦" :
            {"name" : "操縦（" + chara["main_souju_norimono"] + "）",
             "value" : chara["TAAP"][6]},
          "跳躍" :
            {"name" : "跳躍",
             "value" : chara["TAAP"][7]},
          "電気修理" :
            {"name" : "電気修理",
             "value" : chara["TAAP"][8]},
          "ナビゲート" :
            {"name" : "ナビゲート",
             "value" : chara["TAAP"][9]},
          "変装" :
            {"name" : "変装",
             "value" : chara["TAAP"][10]},
          #行動技能で独自のものを追加した場合ここに入る可能性がある（未対応）

          "言いくるめ" :
            {"name" : "言いくるめ",
             "value" : chara["TCAP"][0]},
          "信用" :
            {"name" : "信用",
             "value" : chara["TCAP"][1]},
          "説得" :
            {"name" : "説得",
             "value" : chara["TCAP"][2]},
          "値切り" :
            {"name" : "値切り",
             "value" : chara["TCAP"][3]},
          "母国語" :
            {"name" : "母国語（" + chara["mylang_name"] + "）",
             "value" : chara["TCAP"][4]},
          #交渉技能で独自のものを追加した場合ここに入る可能性がある（未対応）

          "医学" :
            {"name" : "医学",
             "value" : chara["TLAP"][0]},
          "オカルト" :
            {"name" : "オカルト",
             "value" : chara["TLAP"][1]},
          "化学" :
            {"name" : "化学",
             "value" : chara["TLAP"][2]},
          "クトゥルフ神話" :
            {"name" : "クトゥルフ神話",
             "value" : chara["TLAP"][3]},
          "芸術" :
            {"name" : "芸術（" + chara["geijutu_bunya"] + "）",
             "value" : chara["TLAP"][4]},
          "経理" :
            {"name" : "経理",
             "value" : chara["TLAP"][5]},
          "考古学" :
            {"name" : "考古学",
             "value" : chara["TLAP"][6]},
          "コンピューター" :
            {"name" : "コンピューター",
             "value" : chara["TLAP"][7]},
          "心理学" :
            {"name" : "心理学",
             "value" : chara["TLAP"][8]},
          "人類学" :
            {"name" : "人類学",
             "value" : chara["TLAP"][9]},
          "生物学" :
            {"name" : "生物学",
             "value" : chara["TLAP"][10]},
          "地質学" :
            {"name" : "地質学",
             "value" : chara["TLAP"][11]},
          "電子工学" :
            {"name" : "電子工学",
             "value" : chara["TLAP"][12]},
          "天文学" :
            {"name" : "天文学",
             "value" : chara["TLAP"][13]},
          "博物学" :
            {"name" : "博物学",
             "value" : chara["TLAP"][14]},
          "物理学" :
            {"name" : "物理学",
             "value" : chara["TLAP"][15]},
          "法律" :
            {"name" : "法律",
             "value" : chara["TLAP"][16]},
          "薬学" :
            {"name" : "薬学",
             "value" : chara["TLAP"][17]},
          "歴史" :
            {"name" : "歴史",
             "value" : chara["TLAP"][18]},
          #知識技能で独自のものを追加した場合ここに入る可能性がある（未対応）
        }
    }

    # キャラデータの保存
    print('Chara_data save now')
    fc.file_writer(new_chara_json, unique_id)

    # 一時ファイルの削除
    fc.file_json_deleter(tmp_id)

    return new_chara_json

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

def skill_outputer(data, skill):
    put_result = ( '\nPC名 '+data['name']+'\n'+data['skill'][skill]['name'] + ' ' + data['skill'][skill]['value'])
    print(put_result)
    return put_result

if __name__ == '__main__':
    test()

print('success status controller load')
