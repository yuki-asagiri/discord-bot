import json

def dice_json_is_secret(json):
    dice_result = json
    secret = '||'
    print(type(dice_result['secret']))

    if dice_result['secret']:
        dice_result['result'] = secret + dice_result['result'] + secret
    return dice_result

def dice_json_outputer(json):
    print_message = json['result']
    return print_message