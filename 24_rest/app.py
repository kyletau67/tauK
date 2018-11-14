'''Kyle Tau
SoftDev1 pd6
K24 -- A RESTful Journey Skyward
2018-11-13'''

from flask import Flask,render_template
import urllib, json
app = Flask(__name__)

@app.route("/")
def go():
    r = urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=motrt4z0moLTYLk3ziqhyD8KCZsf6k4n8EwJcBN0').read()
    dict = json.loads(r)
    return render_template('page.html', pic = r['url'])

if __name__ == "__main__":
    app.debug = True
    app.run()
