#Kyle Tau
#SoftDev pd 6
#K13 -- Echo Echo Echo
#2018-09-28


from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def go():
    return render_template("fields.html")
    print(app)

@app.route("/auth")
def authenticate():
    print(app)
    #print(request)
    #print(request.args)
    print(request.args['username'])
    print(request.headers)
    return render_template("response.html",
			name = request.args['username'])
    
if __name__ == "__main__":
    app.debug = True
    app.run()
