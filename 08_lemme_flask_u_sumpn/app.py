#Kyle Tau
#SoftDev1 pd 6
#K08 -- Fill Yer Flask
#2018-09-18

from flask import Flask,render_template
app = Flask(__name__)

#render_template("./template/template_html_file.html")

coll = {0,1,1,2,3,5,8}
@app.route("/")
def route0():
    return "Simplicity is divine."

@app.route("/r1")
def route1s():
    return "Note anything notable."

@app.route("/r2")
def route2():
    return "Use QAF liberally."

@app.route("/my_foist_template")
def test_tmplt():
    return render_template('template_html_file.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
