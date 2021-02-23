import base64
from Crypto.Cipher import AES

key = 'assignmentToSetu'
 
def to_16(value):

    while len(value) % 16 != 0:
        value += '\0'

    return str.encode(value)

def encrypt(text):
    
    aes = AES.new(key, AES.MODE_ECB)
    encrypt_aes = aes.encrypt(to_16(text))
    encrypted_text = str (base64.encodebytes(encrypt_aes))
    return encrypted_text

def decrypt(text):
    aes = AES.new(to_16(key), AES.MODE_ECB)
    decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
    decrypted_text = str(aes.decrypt(decrypted),encoding='utf-8').replace('\0','')
    return decrypted_text
 
if __name__ == '__main__':

    text = '{"data": {"loan_number":"BAS123JKE",},"checksum": "4406f3578082e33d1b16c0a7da74d2eb921eab48"}'
    entrypted_text = encrypt(text)
    decrypted_text = decrypt("35O+Ss56p7jQCOxuUZQX2qCnuI321cVFJbmnKypTufEC7VejyTTsqJsGixgggsjG4bxVIr8CPz46 NJjMA/25SrrP/4HsucYsMzAkOFOFGyKfEGTs3lk1RDnWWL/hA4wWnHrzDs5JgmUoz+h+rDZWr n6XVAQzUQ1bQMAqDbggyQwCJs9NzhcU2QN7gCg0FAaFdM3TSzoqm+NpAyetdPMrWw==")

    print('Entrypted Text : ',entrypted_text)
    print('Decrypted Text : ',decrypted_text)
