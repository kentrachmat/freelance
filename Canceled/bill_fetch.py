from encryption_AES256 import *
import requests
import hashlib
import json


url = 'https://4hfvpey3dk.execute-api.ap-south-1.amazonaws.com/v1/bill-apis/stage/modules/module/bbps/bills/fetch'

def hash_encryption(data):
    hashed = hashlib.sha1(data.encode())
    return hashed.hexdigest()

def fetch_bill(loan):
    datas     = '{"data": {"loan_number":'+'"'+loan+'"'+',},"checksum":'+'"'+hash_encryption(loan)+'"'+'}'
    encrypted = encrypt(datas)
    headers   = {'Content-type': 'application/json'}
    requested = requests.post(url,data = encrypted, headers = headers)
    print(decrypt(requested.text))
    return (requested.status_code)


print(fetch_bill('BAS123JKE'))