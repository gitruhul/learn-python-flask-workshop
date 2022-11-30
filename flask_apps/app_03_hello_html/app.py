from flask import Flask
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/hello')
def hello():
    return "<h1>Hello!</h1>"

@app.route('/hi/')
def hi():
    return """
    <h1>This is heading 1</h1>
    <h2>This is heading 2</h2>
    <h3>This is heading 3</h3>
    <a href="https://www.w3schools.com">This is a link</a>
    <p> This is a paragraph!</p>
    """

@app.route('/data/')
def data():
    now_utc = datetime.now(timezone('UTC'))
    now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
    format = "%Y-%m-%d %H:%M:%S %Z"
    ist_date = now_asia.strftime(format)
    return {
        "message": "Hello Flask Devs",
        "date": ist_date
    }

if __name__ == '__main__':
    app.run(debug=True, port=8083)
