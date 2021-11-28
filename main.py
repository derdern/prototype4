from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def base():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM tbl_add_user_data').fetchall()
    conn.close()
    return render_template("index.html",data=data)



@app.route("/add_data")
def add_data():
    return render_template("add_data.html")


@app.route("/personal")
def personal():
    return render_template("personal.html")


@app.route("/morning")
def morning():
    return render_template("morning.html")


@app.route("/ok_data",methods=['POST'])
def okdata():
    dish_text = request.form['dish']
    return render_template("ok_data.html",text=dish_text)


@app.route("/confirmmorning")
def confirmmorning():
    return render_template("confirmmorning.html")


@app.route("/lunch")
def lunch():
    return render_template("lunch.html")


@app.route("/confirmlunch")
def confirmlunch():
    return render_template("confirmlunch.html")


@app.route("/dinner")
def dinner():
    return render_template("dinner.html")


@app.route("/confirmdinner")
def confirmdinner():
    return render_template("confirmdinner.html")


# if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8080, debug=True)
