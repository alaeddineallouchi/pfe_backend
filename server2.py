from flask import Flask 

app = Flask(__name__)


@app.route("/")
def welcome() : 
    return"Hello_World"


@app.route("/temp")
def temp() : 
    return"temp is 20 deg"

@app.route("/humidity")
def humidity() : 
    return"yes or no "

@app.route("/smoke")
def smoke() : 
    return"no smoke "

@app.route("/movement")
def movement() : 
    return"yes or no "

if (__name__=="__main__") : 
    app.run(host="0.0.0.0")
