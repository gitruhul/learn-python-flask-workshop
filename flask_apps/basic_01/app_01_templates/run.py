from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('hello.html')

@app.route('/<user>')
def hello_name(user):
   return render_template('hello.html', name = user)

@app.route('/<user>/<int:score>')
def result(user, score):
   return render_template('marks_result.html', name = user, marks = score)

if __name__ == '__main__':
   app.run(debug = True)

"""
{% ... %} for Statements
{{ ... }} for Expressions to print to the template output
{# ... #} for Comments not included in the template output
# ... ## for Line Statements
"""