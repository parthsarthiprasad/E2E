import cv2
import requests
import numpy as np
import os
import time
from requests.exceptions import ConnectionError

class Predictor:
    def __init__(self,name=os.getlogin()):
        self.name = name
        self.url = "http://127.0.0.1:5000/"  #i.e. http://x.y.z.w/ last / is necessary
        self.name_url = self.url+"name/"+name
        self.count=1
        try:
            resp = requests.post(self.url,{"user_name":self.name})
        except ConnectionError:
            print("Internal Error: Failed to connect to server")
    
    def get_pred(self,frame):
        _, img_encoded = cv2.imencode('.jpg', frame)
        try:
            resp_1 = requests.post(self.name_url,{"image":frame.tostring(),"count":self.count})
            time.sleep(0.05)
            resp_2 = requests.get(self.name_url).json()
        except ConnectionError:
            print("Internal Error: Failed to connect to server")
            return -1
        img = cv2.imdecode(np.fromstring(resp_2["image"],np.uint8),cv2.IMREAD_COLOR)
        return img
