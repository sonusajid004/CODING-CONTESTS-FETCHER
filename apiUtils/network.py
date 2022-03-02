import requests

def post(url:str,json:str):
    r = requests.post(url, json=json)
    return r

def get(url:str):
    r = requests.get(url)
    return r

