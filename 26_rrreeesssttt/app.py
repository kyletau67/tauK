#Kyle Tau
#SoftDev1 pd6
#K26 -- Getting More REST
#2018-11-15

import json, urllib

from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def go():

    url = 'https://ipapi.co/json/'
    r = urllib.request.urlopen(url).read()
    dict = json.loads(r)
    print(dict)
    ip = dict['ip']
    region = dict['region']
    country = dict['country']
    lat = dict['latitude']
    lon = dict['longitude']
    org = dict['org']
    print('=================================')
    quoteapi = 'https://favqs.com/api/qotd'
    r = urllib.request.urlopen(quoteapi).read()
    dict = json.loads(r)
    print(dict)
    quote= dict['quote']['body']
    print('=================================')
    dog = 'https://dog.ceo/api/breeds/image/random'
    r = urllib.request.urlopen(dog).read()
    dict = json.loads(r)
    print(dict)
    dogPic= dict['message']

    return render_template('page.html',
                               ip=ip,
                               region=region,
                               country=country,
                               lat=lat,
                               lon=lon,
                               org=org,
                               quote=quote,
                               pic=dogPic)

if __name__ == "__main__":
    app.debug = True
    app.run()
