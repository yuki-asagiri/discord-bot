import requests
import glob
import json
import urllib.request
import os

def test():
    print('直接読まないで')

def list_in_message(message, lolist):
    for i in lolist:
        if i in message:
            return True

def list_in_ob(message, lolist):
    for i in lolist:
        if i in message:
            return i

# valで指定した値にステータスを変更する
def status_converter(status, unique_id, val):
    chara = chara_loader(unique_id)
    chara['status'][status] = val

    f = open('path/chara_data/'+chara["unique_id"]+'.json', 'w')
    json.dump(chara, f)

    return chara

# valで指定した値だけステータスを増減する
def status_converter2(status, unique_id, val):
    chara = chara_loader(unique_id)
    chara['status'][status] = str(int(chara['status'][status]) + int(val))

    f = open('path/chara_data/'+chara["unique_id"]+'.json', 'w')
    json.dump(chara, f)

    return chara

def chara_loader(unique_id):
    file_path = 'path/chara_data/'
    chara_name = str(unique_id) + '.json'
    data_path = file_path + chara_name

    with open(data_path) as f:
        s = f.read()
    result = json.loads(s)
    return result

def chara_lister():
    dir_path = 'path/chara_data/'
    file_list = glob.glob(dir_path+'*')
    pc_name_list = []
    for file_name in file_list:
       pc_name_list.append(file_name.split('.')[0].split('/')[2])
    print(pc_name_list)

    return pc_name_list

def chara_data_download(id_url):
    print('download読み込み')
    chara_id = 'path/chara_data/malmalmalmal.json'

    # return urllib.request.urlretrieve(id_url, chara_id)
    response = requests.get(id_url)
    print(response)
    chara_data = urllib.request.urlretrieve(id_url, chara_id)

    return chara_data

def chara_data_extracter(unique_id):

    with open('path/chara_data/malmalmalmal.json') as f:
        s = f.read()
    chara = json.loads(s)
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
        }
    }

    f = open('path/chara_data/'+new_chara_json["unique_id"]+'.json', 'w')
    json.dump(new_chara_json, f)

    os.remove('path/chara_data/malmalmalmal.json')

    return new_chara_json

def chara_data_output(unique_id, form):
    id = unique_id
    dir_path = 'path/chara_data/'
    file_path = dir_path + id + '.json'
    if not os.path.isfile(file_path):
        return 'キャラクターがいません'
    else:
        with open(file_path, 'r') as f:
            s = f.read()
        chara_data = json.loads(s)
        return outputer(chara_data, form)

def outputer(data, form):
    if form == 'full':
        put_result = (  'PC名 '+data['name']+'\n'
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
        put_result = (  'PC名 '+data['name']+'\n'+status + data['status'][form])
    print(put_result)
    return put_result

if __name__ == '__main__':
    test()

print('success file load')
