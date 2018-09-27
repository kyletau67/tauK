from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def go():
    render_template("fields.html")
    print(app)

@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.args)
    return "Waaaa hooo HAAAH"
    
if __name__ == "__main__":
    app.debug = True
    app.run()
