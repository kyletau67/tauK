#Britni Canale and Kyle Tau
#SoftDev1 pd 6
#K14 -- Do I Know You?
#2018-10-01

from flask import Flask, render_template, session, request, url_for, redirect
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)
uname = "tom"
pword = "jerry"

@app.route("/")
def login():
    if 'username' not in session:
        return render_template("login.html")
    return redirect(url_for('welcome'))

@app.route("/welcome", methods=["POST"])
def welcome():
    un = request.form["uname"]
    pw = request.form["pword"]
    if un == "tom" and pw == "jerry":
        session['username'] = uname
        return render_template("welcome.html", uname = request.form["uname"])
    return render_template("error.html")

@app.route("/logout")
def go():
    if 'username' in session:
        session.pop['username']
    return "You have logged out."

if __name__ == "__main__":
    app.debug = True
    app.run()
