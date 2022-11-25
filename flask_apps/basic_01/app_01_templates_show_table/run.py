from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/',methods = ['POST'])
def index():
   if request.method == 'POST':
      return render_template('show_table.html', result = request.get_json())


if __name__ == '__main__':
   app.run(debug = True)

"""
{% ... %} for Statements
{{ ... }} for Expressions to print to the template output
{# ... #} for Comments not included in the template output
# ... ## for Line Statements
"""