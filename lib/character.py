
class Character():
    # クラス変数
    # 保管所フォーマットのjsonにおいて、技能値が保存されているキー
    skill_group_list = ['TBAP', 'TFAP', 'TAAP', 'TCAP', 'TKAP']
    # 保管所フォーマットのjsonにおいて、独自で追加した技能の技能名が保管されているキー
    originalskill_name_list = ['TBAName', 'TFAName', 'TAAName', 'TCAName', 'TKAName']
    # 保管所フォーマットのjsonにおける、技能の登録順序
    skill_name_list = {
        'TBAP' : ['回避', 'キック', '組み付き', 'パンチ', '頭突き', '投擲', 'マーシャルアーツ', '拳銃', 'サブマシンガン', 'ショットガン', 'マシンガン', 'ライフル'],
        'TFAP' : ['応急手当', '鍵開け', '隠す', '隠れる', '聞き耳', '忍び歩き', '写真術', '精神分析', '追跡', '登攀', '図書館', '目星'],
        'TAAP' : ['運転', '機械修理', '重機械操作', '乗馬', '水泳', '製作', '操縦', '跳躍', '電気修理', 'ナビゲート', '変装'],
        'TCAP' : ['言いくるめ', '信用', '説得', '値切り', '母国語'],
        'TKAP' : ['医学', 'オカルト', '化学', 'クトゥルフ神話', '芸術', '経理', '考古学', 'コンピューター', '心理学', '人類学', '生物学', '地質学', '電子工学', '天文学', '博物学', '物理学', '法律', '薬学', '歴史']
    }

    @property
    def name(self):
        return self._name

    @property
    def unique_id(self):
        return self._unique_id

    # キャラのステータス値を返す
    def get_status_value(self, item):
        print('TODO: [Character::get_status_value()] 未定義のステータスが指定された場合のエラーハンドリングをする')
        return self.status[item]

    # キャラのステータス値を設定
    # 必要に応じて、技能値（＜アイデア＞等）も更新
    # 何も返さない
    def set_status_value(self, item, value):
        print('TODO: [Character::set_status_value()] 未定義の技能が指定された場合のエラーハンドリングをする')
        self.status[item] = value

        # 技能値を更新する必要があるケース = POW, INT, EDU, SAN
        if item == 'POW':
            self.skill['幸運']['value'] = str(int(self.status['POW']) * 5)
        elif item == 'INT':
            self.skill['アイデア']['value']= str(int(self.status['INT']) * 5)
        elif item == 'EDU':
            self.skill['知識']['value'] = str(int(self.status['EDU']) * 5)
        elif item == 'SAN':
            self.skill['SAN']['value'] = str(int(self.status['SAN']))


    # キャラの技能値を返す
    def get_skill_value(self, skillname):
        print(self.name + ':' + skillname + ' ' + self.skill[skillname]['value'])
        return self.skill[skillname]['value']


    # キャラの技能値を設定
    def set_skill_value(self, skillname, value):
        self.skill[skillname]['value'] = value

    # キャラの技能名（表示名）を返す
    def get_skill_name(self, skillname):
        return self.skill[skillname]['name']

    # コンストラクタ
    # data: 保管所形式のjsonデータまたはDBからの読み出しデータ
    # data_source: hokanjo または db
    def __init__(self, unique_id, data, data_source):
        if data_source == 'hokanjo':
            print('[character] create new character ' + unique_id + ' from hokanjo.')

            self.status = {}
            self.skill = {}

            # 基本的な部分の変換
            self._unique_id = unique_id # 一応こっちにも持たせているが必要かどうかは不明
            self._name = data['pc_name']

            self.status['STR'] = data['NA1']
            self.status['CON'] = data['NA2']
            self.status['POW'] = data['NA3']
            self.status['DEX'] = data['NA4']
            self.status['APP'] = data['NA5']
            self.status['SIZ'] = data['NA6']
            self.status['INT'] = data['NA7']
            self.status['EDU'] = data['NA8']
            self.status['HP'] = data['NA9']
            self.status['MAXHP'] = data['NA9']
            self.status['MP'] = data['NA10']
            self.status['MAXMP'] = data['NA10']
            self.status['SAN'] = data['NA11']
            self.status['idea'] = data['NA12']
            self.status['幸運'] = data['NA13']
            self.status['知識'] = data['NA14']
            self.status['DB'] = data['dmg_bonus']

            # 基本的なスキルの読み込み
            for skill_group in Character.skill_group_list:
                # 各スキルグループごとに、技能名ガン回し
                for index, skill_name in enumerate(Character.skill_name_list[skill_group]):
                    skill_json = {
                        "name" : skill_name,
                        "value" : data[skill_group][index]
                    }
                    self.skill[skill_name] = skill_json

            # 独自追加技能の反映
            # 独自追加の技能があるかを調べ、ある場合は追加する
            # 独自追加技能の名前はTBAName, TFAName,TAAName, TCAName, TKANameにそれぞれある。
            for group_index, name_group in enumerate(Character.originalskill_name_list):
                if name_group in data:
                    for skill_index, skill_name in enumerate(data[name_group]):
                        print('orijinal skill > ' + skill_name)
                        skill_json = {
                            "name" : skill_name,
                            "value" : data[Character.skill_group_list[group_index]][len(Character.skill_name_list[Character.skill_group_list[group_index]])+skill_index]
                        }
                        self.skill[skill_name] = skill_json

            # 一部の技能（芸術等）の表示名変更
            self.skill['運転']['name'] = "運転（" + data["unten_bunya"] + "）"
            self.skill['製作']['name'] = "制作（" + data["seisaku_bunya"] + "）"
            self.skill['操縦']['name'] = "操縦（" + data["main_souju_norimono"] + "）"
            self.skill['母国語']['name'] = "母国語（" + data["mylang_name"] + "）"
            self.skill['芸術']['name'] = "芸術（" + data["geijutu_bunya"] + "）"

            # ステータス依存技能の設定
            luck = {"name" : "幸運", "value" : str(int(self.status["POW"]) * 5)}
            self.skill['幸運'] = luck
            knowledge = {"name" : "知識", "value" : str(int(self.status["EDU"]) * 5)}
            self.skill['知識'] = knowledge
            idea = {"name" : "アイデア", "value" : str(int(self.status["INT"]) * 5)}
            self.skill['アイデア'] = idea
            san = {"name" : "SAN", "value" : str(int(self.status["SAN"]))}
            self.skill['SAN'] = san

        if data_source == 'db':
            print('TODO [character::Character()] コンストラクタで、data_source=dbはまだ未実装')
            return
