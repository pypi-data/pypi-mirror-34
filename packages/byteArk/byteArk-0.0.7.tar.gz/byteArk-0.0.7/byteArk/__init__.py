name = "ByteArk Project"

import requests
import json

class Vision:
   
    def __init__(self):
        print("Vision Initial . . .")
    
    def face_recognition_image(self, file_name):
        url = "http://103.253.132.67:61119/test_image"
        files = {'file': open(file_name, 'rb')}
        r = requests.post(url, files=files)
        res = json.loads(r.text)['result']
        num_dara = len(res)
        if num_dara == 0:
           print("No face detected")
        elif num_dara == 1:
           print("There is 1 face detected")
        else:
           print("There are "+str(num_dara)+" faces detected")
        count = 1
        for ir in res:
            print(str(count)+" : "+ir['Name'])
            print("\t Confidential Value :"+str(ir['Accuracy']))
            print("\t Position : ")
            print("\t\t (x0, y0) : ("+str(ir['X0'])+","+str(ir['Y0'])+")")
            print("\t\t (x1, y1) : ("+str(ir['X1'])+","+str(ir['Y1'])+")")  
            count = count + 1
        return
        #return res
