import os
import json

def test():
    print('ファイルの操作ファイル')

def file_writer(character_json, unique_id):
    dir_path = 'path/chara_data/'
    chara_name = str(unique_id) + '.json'
    data_path = dir_path + chara_name
    
    with open(data_path, 'w') as f:
        json.dump(character_json, f)
    print('write success')

def file_reader(unique_id):
    dir_path = 'path/chara_data/'
    chara_name = str(unique_id) + '.json'
    data_path = dir_path + chara_name
 
    if not os.path.isfile(data_path):
        return 'キャラクターがいないっす。'
    else:
        with open(data_path, 'r') as f:
            s = f.read()
        chara_data = json.loads(s)
    print('read success')

    return chara_data

def file_json_deleter(unique_id):
    dir_path = 'path/chara_data/'
    chara_name = str(unique_id) + '.json'
    data_path = dir_path + chara_name

    os.remove(data_path)

if __name__ == '__main__':
    test()

print('success file controller load')
