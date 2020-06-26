import requests
import json
import traceback

# 指定のURL（キャラクター保管所）に接続してjsonを取得する
# @return 取得した保管所形式のjsonファイル
def download_from_hokanjo(url):
    print('[hokanjo_handler]: connect to キャラクター保管所')
    headers = {"content-type": "application/json"}
    req = url
    response = requests.get(req, headers=headers)
    try:
        data = response.json()
        print('[hokanjo_handler]: connection success.\n download ' + url)
    except Exception:
        print('[hokanjo_handler]: connection failure')
        traceback.print_exc()
        data = None
    return data
