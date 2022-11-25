from flask import Flask, request
app = Flask(__name__)


@app.route('/',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      return {
        "message": "You have sent a POST request",
        }
   else:
      return "You have sent a GET request"

if __name__ == '__main__':
   app.run(debug = True)