#Kyle Tau
#SoftDev1 pd 6
#K08 -- Fill Yer Flask
#2018-09-18

from flask import Flask
app = Flask(__name__)

@app.route("/")
def route0():
    return "Simplicity is divine."

@app.route("/r1")
def route1s():
    return "Note anything notable."

@app.route("/r2")
def route2():
    return "Use QAF liberally."

if __name__ == "__main__":
    app.debug = True
    app.run()