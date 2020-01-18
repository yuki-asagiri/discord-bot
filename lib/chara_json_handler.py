import json

# キャラクターデータ保管用のjson操作ファイル

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

# 保管所フォーマットのjsonをこのbotのchara_jsonフォーマットに変換する
def convert_hokanjo_format_to_charajson(hokanjo):

    # 基本的な部分の変換
    charajson = {
      "name" : hokanjo["pc_name"],
      "unique_id" : unique_id,
      "status" : {
        "STR"  : hokanjo["NA1"],
        "CON"  : hokanjo["NA2"],
        "POW"  : hokanjo["NA3"],
        "DEX"  : hokanjo["NA4"],
        "APP"  : hokanjo["NA5"],
        "SIZ"  : hokanjo["NA6"],
        "INT"  : hokanjo["NA7"],
        "EDU"  : hokanjo["NA8"],
        "HP"   : hokanjo["NA9"],
        "MP"   : hokanjo["NA10"],
        "SAN"  : hokanjo["NA11"],
        "idea" : hokanjo["NA12"],
        "幸運" : hokanjo["NA13"],
        "知識" : hokanjo["NA14"]
      }
    }

    # 基本的なスキルの読み込み
    for skill_group in skill_group_list:
        # 各スキルグループごとに、技能名ガン回し
        for index, skillname in enumarate(skill_name_list[skill_group]):
            charajson['skill'][skillname]['name'] = skillname
            charajson['skill'][skillname]['value'] = hokanjo[skillgroup][index]

    # 独自追加技能の反映
    # 独自追加の技能があるかを調べ、ある場合は追加する
    # 独自追加技能の名前はTBAName, TFAName,TAAName, TCAName, TKANameにそれぞれある。

    return charajson
