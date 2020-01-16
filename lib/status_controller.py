import json
from lib import character_controller as cc

def test():
    print('これはやめて')

# valで指定した値にステータスを変更する
def status_converter(status, unique_id, val):
    chara = cc.chara_loader(unique_id)
    chara['status'][status] = val

    # ここでファイル更新
    cc.chara_saver(chara, unique_id)

    return chara

# valで指定した値だけステータスを増減する
def status_converter2(status, unique_id, val):
    chara = cc.chara_loader(unique_id)
    chara['status'][status] = str(int(chara['status'][status]) + int(val))

    # ここでファイル更新
    cc.chara_saver(chara, unique_id)

    return chara

# 増減を判断する
def is_initial_sign(num: str):
    if num[0] == '+' or num[0] == '-':
        return True
    else:
        return False
