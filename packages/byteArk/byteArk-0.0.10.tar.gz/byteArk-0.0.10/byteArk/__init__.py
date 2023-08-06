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
        img_id = json.loads(r.text)['id']
        print("Image id : "+str(img_id))
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
        #return
        return  json.loads(r.text)

    def get_original_image(self, id):
        url = "http://103.253.132.67:61119/get_original_image/"+str(id)
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(id+"_originalImage.png", 'wb') as f:
                for chunk in r:
                    f.write(chunk)
            print("Save image : "+str(id)+"_originalImage.png")
        else:
            print("Invalid image id . . . ")

    def get_result_image(self, id):
        url = "http://103.253.132.67:61119/get_test_image/"+str(id)
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(id+"_resultImage.png", 'wb') as f:
                for chunk in r:
                    f.write(chunk)
            print("Save image : "+str(id)+"_resultImage.png")
        else:
            print("Invalid image id . . . ")

    def get_face_image(self, img_id, face_id):
        url = "http://103.253.132.67:61119/get_crop_image/"+str(img_id)+"/"+str(face_id)
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(str(img_id)+"_faceImage"+str(face_id)+".png", 'wb') as f:
                for chunk in r:
                    f.write(chunk)
            print("Save image : "+str(img_id)+"_faceImage"+str(face_id)+".png")
        else:
            print("Invalid image id . . . ")

    def face_recognition_video(self, file_name):
        url = "http://103.253.132.67:61119/test_video_draw"
        files = {'file': open(file_name, 'rb')}
        r = requests.post(url, files=files, data={'fps': 5})
        video_id = json.loads(r.text)['id']
        print(video_id)
        return video_id

    def get_video_status(self, video_id):
        url = "http://103.253.132.67:61119/get_test_video_status/"+str(video_id)
        r = requests.get(url, stream=True)
        status = json.loads(r.text)['status']
        print(status)
        return status

    def get_original_video(self, id):
        url = "http://103.253.132.67:61119/get_test_video/"+str(id)
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(id+"_originalVideo.mp4", 'wb') as f:
                for chunk in r:
                    f.write(chunk)
            print("Save video : "+str(id)+"_originalVideo.mp4")
        else:
            print("Invalid video id . . . ")

    def get_result_video(self, id):
        url = "http://103.253.132.67:61119/get_test_video_result/"+str(id)
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(id+"_resultVideo.mp4", 'wb') as f:
                for chunk in r:
                    f.write(chunk)
            print("Save video : "+str(id)+"_resultVideo.mp4")
        else:
            print("Invalid video id . . . ")
