#Kyle Tau
#SoftDev1 pd6
#K25 -- Getting More REST
#2018-11-14

import json, urllib

from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def go():
    root = 'https://www.food2fork.com/api/get?key='
    key = 'fdb328de229db1e1563bb0e297e28cb9'
    id = '&rId=42801' #search id for artichoke and scallion dip
    url = 'https://ipapi.co/json/'
    r = urllib.request.urlopen(url).read()
    dict = json.loads(r)
    print(dict)
    return render_template('page.html',
                               ip=dict['ip'],
                               region=dict['region'],
                               country=dict['country'],
                               lat=dict['latitude'],
                               lon=dict['longitude'],
                               org=dict['org'])

if __name__ == "__main__":
    app.debug = True
    app.run()
