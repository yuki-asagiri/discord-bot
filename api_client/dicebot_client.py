import urllib.parse
import requests
import json
import re
from lib import json_extracter as je

def string_analyze(message):
    search_ccb = re.search(r'(b|B|c|C|e|E)(c|C|r|R|s|S)(b|B)', message)
    search_dice = re.search(r'([0-9]+)[dD]([0-9\ ]+)', message)

    return true_or_false(search_ccb or search_dice)

def true_or_false(proposition):
    if proposition:
        return True
    else:
        return False

def request_creater(message):
    host = 'localhost'
    port = '9292'
    system = 'Cthulhu'

    url = '/v1/diceroll'
    para = '?system=' + system + '&command=' + urllib.parse.quote(message.replace(' ', ''))

    fqdn = 'http://' + host + ':' + port + url + para + ''
    print('To request ⇛' + fqdn)
    return fqdn

def dice_api_client(message):
    req = request_creater(message)
    headers = {"content-type": "application/json"}

    response = requests.get(req, headers=headers)
    try:
        data = response.json()
    except:
        data = False
        return data
    print(data)

    # diceの結果出力ファイル
    out_data = je.dice_json_outputer(je.dice_json_is_secret(data))

    return out_data
