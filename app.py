from flask import Flask, abort, request,jsonify
from bookmyshow import getVenueDataWithUrl, getNowShowing
from json import loads


app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.config["DEBUG"] = True

@app.route('/')
def hello_world():
    print("Jhukadu says hi")
    return "Jhukadu says hi"

@app.errorhandler(404)
def pageNotFound(e):
    print(e)
    return "Error 404, Page not found."

@app.route('/<city>/', methods=["GET", "POST"])
def sendNowShowing(city):
    event = "Movies"
    data = loads(request.data)
    dimensions = None
    languages = None
    x = getNowShowing(city, event, languages, dimensions)
    print(x)
    return 'found some places'

@app.route('/findplaces')
def trial():
    print('Less go')
    exit()

if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0",port=8080)