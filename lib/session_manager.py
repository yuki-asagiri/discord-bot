
from lib import character
from lib import character_manager as cm
from lib import hokanjo_handler
from lib import db_handler

# キャラデータを読み込み、現在のセッションのキャラクターリストに追加する
# urlが空文字列の場合はキャラクター保管所→DBへの読み込みを省略し、データベースからの読み込みのみを実施する
def add_character(bot, unique_id, url):
    if url != '':
        print('[session_manager] add character from hokanjo.')
        # キャラデータ生成
        data = hokanjo_handler.download_from_hokanjo(url)
        if data is None:
            return False
        added_chara = character.Character(unique_id, data, 'hokanjo')

        # dbに保存
        db_handler.write_character(added_chara)
        # キャラクターリストに追加
        cm.add_character(bot, added_chara)
        return True

    else:
        print('[session_manager]: add character from db.')
        print('TODO: [session_manager::add_character()] dbからのキャラ追加は未実装')
