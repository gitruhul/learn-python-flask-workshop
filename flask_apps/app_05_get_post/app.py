import json
import os
from threading import Lock
from flask import Flask, request


app = Flask(__name__)

data_file = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'data.json')

def get_data():
   with open(data_file) as d:
      dictData = json.load(d)
      return dictData

def set_data(data: dict):
   js_file = open(data_file, "w")
   json.dump(data, js_file)
   js_file.close()

@app.route('/',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      json_req = request.get_json()
      #with Lock:
      set_data(json_req)
      return "Succes! Data Updated"
   else:
      return get_data()

if __name__ == '__main__':
   app.run(debug = True, port=8085)