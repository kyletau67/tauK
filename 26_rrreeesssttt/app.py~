#Kyle Tau
#SoftDev1 pd6
#K25 -- Getting More REST
#2018-11-14

import json, ssl

from urllib.request import Request, urlopen
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def go():
    root = 'https://www.food2fork.com/api/get?key='
    key = 'fdb328de229db1e1563bb0e297e28cb9'
    id = '&rId=42801' #search id for artichoke and scallion dip
    url = root+key+id
    print(url)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    r = urlopen(req).read()
    dict = json.loads(r)
    print(dict)
    return render_template('page.html', pic = dict['recipe']['image_url'])

if __name__ == "__main__":
    app.debug = True
    app.run()
