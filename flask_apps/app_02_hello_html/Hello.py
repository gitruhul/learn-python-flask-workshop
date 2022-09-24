from flask import Flask
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
    """

if __name__ == '__main__':
    app.run(debug=True)
