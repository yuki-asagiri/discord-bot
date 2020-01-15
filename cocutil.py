import json

def is_initial_sign(num: str):
    if num[0] == '+' or num[0] == '-':
        return True
    else:
        return False
