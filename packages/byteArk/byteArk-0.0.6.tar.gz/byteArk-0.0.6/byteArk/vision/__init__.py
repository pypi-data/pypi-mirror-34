name = "ByteArk Vision Project"
print(name)

import requests
import json
def face_recognition_image(file_name):
    print("FACE:"+file_name)
    url = "http://103.253.132.67:61119/test_image"
    files = {'file': open(file_name, 'rb')}
    r = requests.post(url, files=files)
    res = json.loads(r.text)['result']
    for ir in res:
        print(ir)
