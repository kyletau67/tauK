from flask import Flask,render_template
import urrlib2, json
app = Flask(__name__)

@app.route("/", methods=["GET"])
def go():
    urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=motrt4z0moLTYLk3ziqhyD8KCZsf6k4n8EwJcBN0')
    return render_template('page.html', pic = ???)

if __name__ == "__main__":
    app.debug = True
    app.run()
