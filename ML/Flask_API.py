from flask import Flask, jsonify, request
from flask_restful import reqparse, Api, Resource
import os
import subprocess
import cv2
import numpy as np
import time

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("image",type=str)
parser.add_argument("count",type=int)

output_dir = "outputs/"

class Main_Page(Resource):
    def __init__(self):
        pass
    
    def get(self):
        return {"Hello":"World"}
    
    def post(self):
        json_data = request.get_json(force = True)
        username = json_data["user_name"]
        os.mkdir(username)
        os.mkdir(output_dir+username)
        p = subprocess.run(["python","Test_2.py",username])
        return {"Happy":"Noises"}

class User_Page(Resource):
    def __init__(self):
        pass
    
    def get(self,name):
        items = os.listdir(output_dir+name)
        while(len(items)==0):
           time.sleep(0.5)
           items = os.listdir(output_dir+name)
        img_name = items[-1]
        img = cv2.imread(output_dir+name+"/"+img_name)
        _, img_encoded = cv2.imencode('.jpg', img)
        return jsonify(image = img_encoded.tolist())
        
    def post(self,name):
        args = request.get_json(force = True)
        image = args["image"]
        count = args["count"]
        np_img = np.array(image,dtype=np.uint8)
        img_decoded = cv2.imdecode(np_img,cv2.IMREAD_COLOR)
        cv2.imwrite(name+"/"+str(count)+".jpg",img_decoded)
        return {"Happy":"Noises"}
        
api.add_resource(Main_Page,"/")
api.add_resource(User_Page,"/name/<string:name>")

if __name__=="__main__":
    app.run(debug=True)