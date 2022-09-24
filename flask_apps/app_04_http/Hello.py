from flask import Flask, redirect, url_for, request
app = Flask(__name__)

app.config["counter"] =  0



@app.route('/counter',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      app.config["counter"] = int(request.form['counter'])
      return app.config["counter"]
   else:
      return str(app.config["counter"])

if __name__ == '__main__':
   app.run(debug = True)