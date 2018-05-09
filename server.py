from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL


app = Flask(__name__)
app.secret_key = "djshbcfw87egt9beu"


mysql = connectToMySQL('friendsDB')


@app.route("/")
def index():
    rec = mysql.query_db("SELECT first_name, last_name, occupation FROM friends")

    return render_template("index.html", data = rec)


@app.route("/register", methods=["post"])
def register():
    fname = request.form["first_name"]
    lname = request.form["last_name"]
    occup = request.form["occupation"]

    if len(fname) <= 0:
        flash("Please enter the first name!")
        fill_session()
        redirect("/")

    if len(lname) <= 0:
        flash("Please enter the last name!")
        fill_session()
        redirect("/")

    if len(occup) <= 0:
        flash("Please enter the occupation!")
        fill_session()
        redirect("/")

    sqlCmd = f"INSERT INTO friends (first_name, last_name, occupation) VALUES ('{fname}', '{lname}', '{occup}')"

    mysql.query_db(sqlCmd)

    return redirect("/")


def fill_session():
    session["first_name"] = request.form["first_name"]
    session["last_name"] = request.form["last_name"]
    session["occupation"] = request.form["occupation"]


if __name__ == "__main__":
    app.run(debug = True)