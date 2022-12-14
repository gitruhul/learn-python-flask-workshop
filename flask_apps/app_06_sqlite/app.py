import os
from flask import Flask, render_template, request
import sqlite3 as sql
from db_utils import init_db, create_table

app = Flask(__name__)

# Init Database
db_name = "database.db"
db_file = os.path.join(os.path.realpath(os.path.dirname(__file__)), db_name)
conn = init_db(db_file=db_file)
create_sql: str = "CREATE TABLE IF NOT EXISTS students (rollno integer primary key autoincrement, name,addr,city,pin)"
create_table(conn=conn, table='students', create_table_sql=create_sql)
conn.close()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew')
def new_student():
    return render_template('student.html')


@app.route('/updateold')
def update_student():
    return render_template('update.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            if nm == "":
                nm = "dummy"
            if addr == "":
                addr = "dummy"
            if city == "":
                city = "dummy"
            if pin == "":
                pin = "000000"

            with sql.connect(db_file) as con:
                cur = con.cursor()

                cur.execute("INSERT INTO students (name,addr,city,pin) VALUES(?, ?, ?, ?)", (nm, addr, city, pin))

                con.commit()
                msg = "Record successfully added"
        except Exception as e:
            con.rollback()
            msg = f"error in insert operation. {e}"

        finally:
            con.close()
            return render_template("result.html", msg=msg)


@app.route('/updaterec', methods=['POST', 'GET'])
def updaterec():
    if request.method == 'POST':
        try:
            update_no = request.form['update_no']

            with sql.connect(db_file) as con:
                cur = con.cursor()

                cur.execute(f"select * from students where rollno = (?)", update_no)
                rows = cur.fetchall()
                print(f"HHHH> {rows}")
                return render_template("list.html", rows=rows)
        except Exception as e:
            con.rollback()
            msg = f"error in update operation. {e}"

        finally:
            con.close()


@app.route('/list')
def list():
    con = sql.connect(db_file)
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall()
    con.close()
    return render_template("list.html", rows=rows)


@app.route('/data')
def data():
    user = request.args.get('node')
    user1 = request.args.get('want')
    if user != "":
        return user + " " + user1


if __name__ == '__main__':
    app.run(port=8086)
