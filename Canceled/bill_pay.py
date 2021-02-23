from encryption_AES256 import *
import requests
import hashlib

url = 'https://4hfvpey3dk.execute-api.ap-south-1.amazonaws.com/v1/bill-apis/stage/modules/module/bbps/bills/receipt'

def hash_encryption(data):
    hashed = hashlib.sha1(data.encode())
    return hashed.hexdigest()

def pay_bill(loan,amount,ref):
    datas     = '{"data": {"loan_number":'+loan+',"fetchId": "fromfetch", "amountPaid":'+amount+',"txnRefId":'+ref+'},"checksum": '+hash_encryption(data)+'}'
    encrypted = encrypt(datas)
    requested = requests.post(url, data = encrypted)
    print(decrypt(requested.text))


print(pay_bill("BAS123JKE",2000,"12312asD"))