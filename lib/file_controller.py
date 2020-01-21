import os
import pickle
import json

def test():
    print('ファイルの操作ファイル')

def file_writer(character_class):
    dir_path = 'path/chara_data/'
    chara_name = character_class.get_unique_id() + '.chara'
    data_path = dir_path + chara_name

    print('TODO: [file_controller.py::file_writer] ファイルオープン時のエラーハンドリング')
    f = open(data_path, 'wb')
    pickle.dump(character_class, f)
    f.close

    print('write success')

def file_reader(unique_id):
    dir_path = 'path/chara_data/'
    chara_name = str(unique_id) + '.chara'
    data_path = dir_path + chara_name

    if not os.path.isfile(data_path):
        return 'キャラクターがいません'
    else:
        print('TODO: [file_controller.py::file_reader] ファイルオープン時のエラーハンドリング')
        f = open(data_path, 'rb')
        chara_data = pickle.load(f)
    print('read success')

    return chara_data

def file_json_deleter(character_class):
    dir_path = 'path/chara_data/'
    chara_name = character_class.get_unique_id() + '.chara'
    data_path = dir_path + chara_name

    os.remove(data_path)

if __name__ == '__main__':
    test()

print('success file controller load')
