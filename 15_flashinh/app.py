#TomJerry - Britni Canale & Kyle Tau
#SoftDev1 pd 6
#K14 -- Do I Know You?
#2018-10-01

from flask import Flask, render_template, session, request, url_for, redirect, flash
import os

app = Flask(__name__)


app.secret_key = os.urandom(32)               #generates random 32-bit secret_key

    
uname = "tom"                                 #HARDCODED USERNAME AND PASSWORD       
pword = "jerry"

@app.route("/")                               #root route, redirects to welcome if logged in, loads login page if not
def login():
    if "username" not in session:
        return render_template("login.html")
    return redirect(url_for("welcome"))


@app.route("/welcome", methods=["POST", "GET"])      #welcome route (if logged in only), EDITonly accepts POST requests
def welcome():
    if "username" not in session:              #checks to see if you were previously logged in or not
        if request.method == "POST":
            un = request.form["uname"]                #gets login info from form
            pw = request.form["pword"]
        else:
            un = request.args["uname"]
            pw = request.args["pword"]
        uncorrect = un == uname                   #creates booleans for username equal and password equal, sent to error to determine error messages
        pwcorrect = pw == pword
        print("<style=\"color:red;\">" + uname + pword)
        if uncorrect and pwcorrect:               #checks username and password, if correct adds to session and renders welcome page and
            session["username"] = uname           #displays error messages if something went wrong, has button to go back to login page
            return render_template("welcome.html", uname = un)
        else:
            if not uncorrect:
                flash("Your username is incorrect")
            if not pwcorrect:
                flash("Your password is incorrect")
            return redirect(url_for("login"))
    return render_template("welcome.html", uname = uname)

@app.route("/logout")                         #route for logging out
def go():
    if 'username' in session:                 #ends session
        session.clear()
    return redirect(url_for("login"))         #redirects to login page after logout


if __name__ == "__main__":
    app.debug = True
    app.run()
